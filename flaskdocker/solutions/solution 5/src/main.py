from flask import Flask, request
from flask_restx import Api, Resource
from sklearn.ensemble import RandomForestClassifier
from sklearn.exceptions import NotFittedError
import numpy as np
import json
from pathlib import Path

app = Flask(__name__)
api = Api(app)

rf = RandomForestClassifier()

def fit_rf_on_dict(data):
    global rf
    rf.fit(np.array(data["X"]).T, data["y"])

@api.route('/fit')
class Fit(Resource):
    def post(self):
        data = request.get_json()
        fit_rf_on_dict(data)
        return "", 204

@api.route('/fitdefault')
class Fit(Resource):
    def get(self):
        data_path = Path(__file__).resolve().parent/ ".." / "data"
        with open(data_path  / "default.json") as f:
            default_data = json.load(f)
        Path(data_path  / "empty").touch()
        fit_rf_on_dict(default_data)
        return "", 200

@api.route('/predict')
class Predict(Resource):
    def post(self):
        data = request.get_json()
        global rf
        try:
            pred = rf.predict(np.array(data["X"]).T)
            return {"predictions": pred}, 200
        except (NotFittedError, ValueError) as e:
            if isinstance(e, NotFittedError):
                return "", 412
            if isinstance(e, ValueError):
                return "", 400

if __name__ == '__main__':
    app.run()
