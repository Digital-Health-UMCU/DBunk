from flask import Flask, request
import numpy as np

app = Flask(__name__)

@app.route('/hello')
def hello_world():
	return 'Hello, World!'

@app.route('/calc')
def calc():
	args = request.args
	if args:
		keys = list(args.keys())
		unaccepted = [i for i in keys if i not in ["square", "double"] ]
		if any(unaccepted):
			return f"Unaccepted queries: {unaccepted}", 400
		else:
			return str([int(v) * 2 if k == "double" else int(v) ** 2 for k, v in args.items()]), 200
	return "No query string received", 200

@app.route('/double/<int:userinput>')
def double(userinput):
	return str(userinput * 2), 200

@app.route('/square/<int:userinput>')
def square(userinput):
	return str(userinput ** 2), 200

@app.route('/fire')
def fire():
	employees = ["Richard", "O'Jay", "Lieke", "Thom", "Sjoerd", "Annemarie", "Marieke"]
	return f"This month, {np.random.choice(employees)} will be fired", 200

var = ""

@app.route('/postthis/<userinput>')
def postthis(userinput):
	global var
	var = userinput
	return "Posted very succesfully", 200

@app.route('/getthat')
def getthat():
	global var
	return var, 200

if __name__ == "__main__":
	app.run(debug=True)
