from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from github actions'

@app.route('/v2')
def v2():
    return 'Second action'

@app.route('/auto')
def auto():
    return 'Hello from auto update'

@app.route('/ssh')
def ssh():
    return 'Hello from auto update with ssh'

@app.route('/snegirev')
def sneg():
    return 'Hello from CI with GitHub Actions by Snegirev'