from config import *

from src.features import run_feature_engineering
from src.preprocess import run_preprocessing

def main():
    df_clean = run_preprocessing(INPUT_DATA_PATH, OUTPUT_DATA_PATH)

    df_model = run_feature_engineering(df_clean, FEATURES_OUTPUT_PATH)

if __name__ == "__main__":
    main()