from flask import Flask
from flask_restx import Api, Resource
from flask_restx.fields import String

app = Flask(__name__)
api = Api(app)

hello_model = api.model("hello_response", {"response": String(enum=["Hello, World!"])})

@api.route('/hello')
class Hello(Resource):
    @api.marshal_with(hello_model)
    def get(self):
        return {"response": 'Hello, World!'}

if __name__ == '__main__':
    app.run()
