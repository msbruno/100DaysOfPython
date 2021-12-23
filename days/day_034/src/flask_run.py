from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p> Hello World </p>"


with app.test_request_context('/'):
    assert request.path == '/'
    assert request.args['name'] == 'Peter'