import pandas as pd

def preprocess_rainfall():

    df = pd.read_csv("data/raw/rainfall.csv")

    df=df.dropna()

    df.to_csv(
    "data/processed/rainfall_clean.csv",
    index=False
    )

if __name__ == "__main__":
    preprocess_rainfall()