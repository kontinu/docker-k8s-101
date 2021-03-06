#!/usr/bin/env python3
import  os,  time, platform
from flask import Flask, make_response, render_template
from functools import wraps, update_wrapper
from datetime import datetime

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def hello():
    host=platform.node()
    DOCKER_SERVICE_NAME=os.getenv('DOCKER_SERVICE_NAME', host)
    if "{{" in DOCKER_SERVICE_NAME or "}}" in DOCKER_SERVICE_NAME:
        DOCKER_SERVICE_NAME="N/A"
    FOO=os.getenv('FOO', 'unset')
    #print(f"Getting visits! {count}")
    return render_template('index.html', hostname=host, DOCKER_SERVICE_NAME=DOCKER_SERVICE_NAME, FOO=FOO )

@app.route('/health')
def health():
    return "Im healthy"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)

