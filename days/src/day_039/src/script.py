from flask import Flask
from redis import Redis

app = Flask(__name__)
count = 0

@app.route("/")
def hello():
    count += 1
    return "Executed {} times".format(count)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
