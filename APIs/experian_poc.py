from flask import Flask, jsonify

experian_poc = Flask(__name__)


@experian_poc.route('/home')
def homepage():
    return jsonify({"Message": "Welcome to the Experian world"})


# if running this file as a script then __name__ = '__main__' is used
if __name__ == '__main__':
    experian_poc.run()
