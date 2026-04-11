import joblib
import os
import pandas as pd


BASE_DIR=os.path.abspath(
os.path.join(os.path.dirname(__file__),"../../")
)

model_path=os.path.join(
BASE_DIR,
"models/rainfall_model.pkl"
)

model=joblib.load(model_path)


def predict_rainfall(data):

    columns=['JUN','JUL','AUG','SEP']

    df=pd.DataFrame([data],columns=columns)

    return model.predict(df)[0]