import joblib

model=joblib.load(
"models/crop_model.pkl"
)

def recommend_crop(features):

    return model.predict([features])[0]