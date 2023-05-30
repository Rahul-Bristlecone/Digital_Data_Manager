from flask import Flask
from flask_profiler import Profiler

logfile = Flask(__name__)

logfile.config["flask_profiler"] = {
    "enabled": logfile.config["DEBUG"],
    "storage": {
        "engine": "sqlite"
    },
    "basicAuth": {
        "enabled": True,
        "username": "admin",
        "password": "admin"
    },
    "ignore": [
        "^/static/.*"
    ]
}

profiler = Profiler()
profiler.init_app(logfile)


@logfile.route('/')
def index():
    return 'Hello, World!'
