import joblib
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
model_path = os.path.join(BASE_DIR, "models", "crop_model.pkl")

model=joblib.load(model_path)

def recommend_crop(features):

    return model.predict([features])[0]