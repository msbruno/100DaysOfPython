from flask import Flask, request

web_app = Flask('web_app')

@web_app.route("/")
def hello_world():
    return "<p> Hello World </p>"

