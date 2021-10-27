from flask import Flask, request
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

@api.route('/double')
class Double(Resource):
    def post(self):
        def double(i):
            if isinstance(i, dict):
                return {k: double(v) for k, v in i.items()}
            elif isinstance(i, list):
                return [double(j) for j in i]
            else:
                return i * 2
        
        return double(request.get_json())

if __name__ == '__main__':
    app.run()
