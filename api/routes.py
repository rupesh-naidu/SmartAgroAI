""" from flask import request, jsonify
import pandas as pd
import os

from src.prediction.rainfall_predictor import predict_rainfall
from src.prediction.crop_predictor import recommend_crop


def register_routes(app):

    # ❌ DO NOT create "/" route here (important)

    @app.route("/full_prediction", methods=["POST"])
    def full_prediction():

        data = request.json

        rainfall = predict_rainfall(
            data["rain_inputs"]
        )

        crop = recommend_crop(
            data["crop_inputs"]
        )

        # save history
        os.makedirs("outputs", exist_ok=True)

        log = pd.DataFrame([{
            "rainfall": rainfall,
            "crop": crop,
        }])

        log.to_csv(
            "outputs/predictions_log.csv",
            mode="a",
            header=False,
            index=False
        )

        return jsonify({
            "rainfall": rainfall,
            "crop": crop,
        }) """

from flask import request, jsonify
import pandas as pd
import os

from src.prediction.rainfall_predictor import predict_rainfall
from src.prediction.crop_predictor import recommend_crop


def register_routes(app):

    @app.route("/full_prediction", methods=["POST"])
    def full_prediction():

        data = request.json

        rainfall = float(predict_rainfall(
            data["rain_inputs"]
        ))

        crop = str(recommend_crop(
            data["crop_inputs"]
        ))

        # save history
        os.makedirs("outputs", exist_ok=True)

        log = pd.DataFrame([{
            "rainfall": rainfall,
            "crop": crop,
        }])

        log.to_csv(
            "outputs/predictions_log.csv",
            mode="a",
            header=False,
            index=False
        )

        return jsonify({
            "rainfall": rainfall,
            "crop": crop,
        })