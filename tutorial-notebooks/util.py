import pandas as pd
import summit


def evaluate_candidates(sample_dataset: pd.DataFrame) -> pd.DataFrame:
    conditions = summit.DataSet.from_df(sample_dataset)
    emulator = summit.get_pretrained_reizman_suzuki_emulator(case=1)
    emulator_output = emulator.run_experiments(conditions, rtn_std=True)
    return emulator_output
