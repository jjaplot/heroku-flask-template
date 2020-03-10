import json
import random
import time
from datetime import datetime

from flask import Flask, Response, render_template


app = Flask(__name__)
random.seed()  # Initialize the random number generator

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graph/')
def graph():
    return render_template('graph.html')



if __name__ == '__main__': app.run(debug=True)
