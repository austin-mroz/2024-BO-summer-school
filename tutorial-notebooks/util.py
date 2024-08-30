"""Utility functions for the tutorial notebooks."""

import numpy as np
import pandas as pd
import summit


def evaluate_candidates(candidates: pd.DataFrame) -> pd.DataFrame:
    """Evaluate the candidates using the Reizman-Suzuki emulator.

    Parameters:
        candidates: A DataFrame with the experiments.

    Returns:
        A DataFrame with the experiments and the predicted yield.
    """
    name_map = {
        "Catalyst Loading": "catalyst_loading",
        "Residence Time": "t_res",
        "Temperature": "temperature",
        "Catalyst": "catalyst",
        "Yield": "yld",
    }
    candidates = candidates.rename(columns=name_map)
    emulator = summit.get_pretrained_reizman_suzuki_emulator(case=1)
    conditions = summit.DataSet.from_df(candidates)
    emulator_output = emulator.run_experiments(
        conditions, rtn_std=True
    ).rename(columns=dict(zip(name_map.values(), name_map.keys())))
    return pd.DataFrame(
        {
            "Catalyst Loading": emulator_output["Catalyst Loading"],
            "Residence Time": emulator_output["Residence Time"],
            "Temperature": emulator_output["Temperature"],
            "Catalyst": emulator_output["Catalyst"],
            "Yield": emulator_output["Yield"],
            "valid_Yield": np.ones(len(emulator_output.index)),
        }
    )
