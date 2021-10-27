from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

@api.route('/double')
class Double(Resource):
    def post(self):
        pass

if __name__ == '__main__':
    app.run()
