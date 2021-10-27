from flask import Flask, redirect, url_for
import numpy as np

app = Flask(__name__)

# @app.route('/')
@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/')
def home_page():
    return redirect(url_for('hello'))

@app.route('/journalclub')
def journal_club():
    team = ["Richard", "O'Jay", "Lieke", "Thom", "Sjoerd", "Leon", "HJ"]
    return f"Next journal club hosted by: {np.random.choice(team)}"

if __name__ == '__main__':
    app.run(debug=True)
