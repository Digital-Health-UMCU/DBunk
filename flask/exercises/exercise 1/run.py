from flask import Flask, redirect, url_for
import numpy as np

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
