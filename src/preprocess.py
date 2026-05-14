"""
preprocess.py

Removes null entries from raw data.

Usage:
    Called from main.py as part of pipeline
Output:
    data/processed/crm_clean.csv
"""

import os
import pandas as pd


def run_preprocessing(input_path: str, output_path: str) -> pd.DataFrame:
    """
    Removes null entries from raw data. Save the updated dataframe separately.

    Args:
        input_path: path to raw data file
        output_path: path to clean data file

    Returns:
        Cleaned dataframe
    """
    df = pd.read_csv(input_path)
    pre_clean_count = df.shape[0]
    df = df.dropna()
    df.reset_index(drop=True, inplace=True)

    print(f"Rows with null values: {pre_clean_count - df.shape[0]}")
    print(f"Rows remaining: {df.shape[0]}")

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    return df
