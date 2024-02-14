import json
from flask import Flask

app = Flask(__name__)


@app.route('/scrappy/streams', methods=['GET'])
def streams():
    return "Hello scrappy"


def run():
    app.run(debug=False, host='0.0.0.0')
