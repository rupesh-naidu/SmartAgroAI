import pandas as pd

def preprocess_crop():

    df=pd.read_csv(
    "data/raw/crop_recommendation.csv"
    )

    df=df.dropna()

    df.to_csv(
    "data/processed/crop_clean.csv",
    index=False
    )

if __name__ == "__main__":
    preprocess_crop()