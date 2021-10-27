from flask import Flask, request
from flask_restx import Api, Resource
from sklearn.ensemble import RandomForestClassifier
from sklearn.exceptions import NotFittedError
import numpy as np

app = Flask(__name__)
api = Api(app)

rf = RandomForestClassifier()

@api.route('/fit')
class Fit(Resource):
    def post(self):
        data = request.get_json()
        global rf
        rf.fit(np.array(data["X"]).T, data["y"])
        return "", 204

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
