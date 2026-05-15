"""
features.py

Module to transform cleaned data into suitable format for the model.
Here, just dropping the identifiers.

Usage:
    Called from main.py as part of the pipeline.
Output:
    data/processed/crm_model.csv
"""

import os
import pandas as pd


def run_feature_engineering(input_df: pd.DataFrame, output_path: str) -> pd.DataFrame:
    """
    Drop identifiers.

    Args:
        input_df: Input cleaned dataframe.
        output_path: Path to model-suitable data file.
    Returns:
        Dataframe with dropped identifiers.
    """

    df = input_df.drop(columns=['journey_id'])

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)

    print(f"Feature engineering complete. Shape: {df.shape}")
    return df