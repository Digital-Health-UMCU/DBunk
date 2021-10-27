from flask import Flask
import numpy as np
from flask_restx import Api, Resource
from flask_restx.fields import String

app = Flask(__name__)
api = Api(app)

hello_model = api.model("hello_response", {"response": String(enum=["Hello, World!"])})

@api.route('/')
@api.route('/hello')
class Hello(Resource):
    @api.marshal_with(hello_model)
    def get(self):
        return {"response": 'Hello, World!'}

team = ["Richard", "O'Jay", "Lieke", "Thom", "Sjoerd", "Leon", "HJ"]
journalclub_model = api.model("journalclub_response", {"response": String(enum=team)})

@api.route('/journalclub')
class JournalClub(Resource):
    @api.marshal_with(journalclub_model)
    def get(self):
        return {"response": np.random.choice(team)}

if __name__ == '__main__':
    app.run(debug=True)
