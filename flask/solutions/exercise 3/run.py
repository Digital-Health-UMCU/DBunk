from flask import Flask, request
from flask_restx import Api, Resource
from flask_restx.fields import Integer, List
from sklearn.ensemble import RandomForestClassifier
from sklearn.exceptions import NotFittedError
import numpy as np

app = Flask(__name__)
api = Api(app)

rf = RandomForestClassifier()

fit_payload = api.model("fit_payload", {"y": List(Integer()), "X": List(List(Integer()))})

@api.route('/fit')
class Fit(Resource):
    @api.expect(fit_payload, validate=True)
    @api.doc(responses={204: "Data received succesfully"})
    def post(self):
        data = request.get_json()
        global rf
        rf.fit(np.array(data["X"]).T, data["y"])
        return "", 204

predict_payload = api.model("predict_payload", {"X": List(List(Integer()))})
predict_model = api.model("predict_response", {"predictions": List(Integer())})

@api.route('/predict')
class Predict(Resource):
    @api.expect(predict_payload, validate=True)
    @api.marshal_with(predict_model)
    @api.doc(responses={200: "Predicted succesfully", 400: "Dimensions inconsistent", 412: "Run /fit first"})
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
