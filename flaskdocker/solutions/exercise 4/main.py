from flask import Flask
from flask_restx import Api, Resource
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)
api = Api(app)

rf = RandomForestClassifier()

@api.route('/fit')
class Fit(Resource):
    def post(self):
        global rf
        pass

if __name__ == '__main__':
    app.run()
