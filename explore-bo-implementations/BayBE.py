"""BayBE implementation of BO."""

import numpy as np
import pandas as pd
from baybe import Campaign
from baybe.objective import Objective
from baybe.parameters import (
    CategoricalParameter,
    NumericalContinuousParameter,
    NumericalDiscreteParameter,
    SubstanceParameter,
)
from baybe.recommenders import (
    RandomRecommender,
    SequentialGreedyRecommender,
    TwoPhaseMetaRecommender,
)
from baybe.searchspace import SearchSpace
from baybe.surrogates import GaussianProcessSurrogate
from baybe.targets import NumericalTarget, TargetMode


def rerun_bo(
    # TODO: what is the type here?
    campaign_db_entry,
    new_measurements: pd.DataFrame,
    batch_size: int = 1,
) -> pd.DataFrame:
    campaign = Campaign.from_json(campaign_db_entry.campaign_info)
    campaign.add_measurements(new_measurements)
    return campaign.recommend(batch_size=batch_size)


def run_bo(
    # TODO: what is the type here?
    experiment_info,
    target: str,
    opt_type: TargetMode = TargetMode.MAX,
    batch_size: int = 1,
) -> tuple[pd.DataFrame, Campaign]:
    variable_type_dict = pd.read_json(experiment_info.variables)
    baybe_paramter_list = []
    for col in variable_type_dict.columns:
        # TODO: type of .T says it returns a Series, but variable is called a DataFrame
        df = variable_type_dict[col].T
        if df["parameter-type"] == "subs":
            baybe_paramter_list.append(
                SubstanceParameter(
                    f"{col}",
                    data=df["json"],
                    # TODO: does df['encoding'] need to be cast to a string?
                    encoding=f"{df['encoding']}",
                )
            )
        elif df["parameter-type"] == "cat":
            baybe_paramter_list.append(
                CategoricalParameter(
                    # TODO: does df['encoding'] need to be cast to a string?
                    f"{col}",
                    values=pd.read_json(df["json"])[f"{col}"],
                    encoding="OHE",
                )
            )
        elif df["parameter-type"] == "int":
            baybe_paramter_list.append(
                NumericalDiscreteParameter(
                    # TODO: does df['encoding'] need to be cast to a string?
                    f"{col}",
                    values=list(
                        np.arange(int(df["min"]), int(df["max"]), 1.0)
                    ),
                )
            )
        else:
            baybe_paramter_list.append(
                NumericalContinuousParameter(
                    # TODO: does df['encoding'] need to be cast to a string?
                    f"{col}",
                    bounds=(float(df["min"]), float(df["max"])),
                )
            )
    search_space = SearchSpace.from_product(baybe_paramter_list)

    objective = Objective(
        mode="SINGLE",
        targets=[NumericalTarget(name=target, mode=opt_type)],
    )

    recommender = TwoPhaseMetaRecommender(
        initial_recommender=RandomRecommender(),
        recommender=SequentialGreedyRecommender(
            surrogate_model=GaussianProcessSurrogate(),
            # TODO: does this need to be cast to a string?
            acquisition_function_cls=f"{experiment_info.acqFunc}",
            allow_repeated_recommendations=False,
            allow_recommending_already_measured=False,
        ),
    )

    campaign = Campaign(
        searchspace=search_space,
        recommender=recommender,
        objective=objective,
    )

    return campaign.recommend(batch_size=batch_size), campaign
