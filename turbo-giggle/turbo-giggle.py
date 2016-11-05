from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/createSession', method='POST')
def create_session():
    pass


@app.route('/form', methods=['POST', 'GET'])
def form():
    pass
