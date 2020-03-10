import json
import random
import time
from datetime import datetime

from flask import Flask, Response, render_template

import paho.mqtt.subscribe as subscribe

def on_message_print(client, userdata, message):
    print("%s %s" % (message.topic, message.payload))

subscribe.callback(on_message_print, "paho/test/callback", hostname="mqtt.eclipse.org")

app = Flask(__name__)
random.seed()  # Initialize the random number generator

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/hello') 
def hello_world():
    return 'Hello, World!'

@app.route('/graph/')
def graph():
    return render_template('graph.html')

@app.route('/users/<name>', methods=['POST'])
def create_user(name):

    msg = f'user {name} created'
    return make_response(msg, 201)

@app.route('/chart-data')
def chart_data():
    def generate_random_data():
        while True:
            json_data = json.dumps(
                {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': random.random() * 100})
            yield f"data:{json_data}\n\n"
            time.sleep(1)

    return Response(generate_random_data(), mimetype='text/event-stream')

if __name__ == '__main__': app.run(debug=True)
