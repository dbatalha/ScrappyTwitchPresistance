from flask import Flask, request

from scrappy_db.presistance.controllers.stream_controller import StreamController
from scrappy_db.presistance.controllers.users_controller import UsersController
from scrappy_db.presistance.controllers.watch_controller import WatchController

app = Flask(__name__)
stream_controller = StreamController()
watch_controller = WatchController()
users_controller = UsersController()


@app.route('/stream', methods=['POST'])
def create_stream():
    return stream_controller.create_stream(request.json)


@app.route('/stream', methods=['PUT'])
def update_stream():
    return stream_controller.update_stream(request.json)


@app.route('/stream', methods=['DELETE'])
def delete_stream():
    return stream_controller.delete_stream(request.args.get('user_name'))


@app.route('/streams', methods=['GET'])
def get_streams():
    return stream_controller.get_all_streams()


@app.route('/watchers', methods=['GET'])
def get_all_watchers():
    return watch_controller.get_all_watchers()


@app.route('/watcher', methods=['POST'])
def add_watcher():
    return watch_controller.add_watcher(request.json)


@app.route('/user', methods=['POST'])
def save_user():
    return users_controller.save_user(request.json)


def run():
    app.run(debug=False, host='0.0.0.0', port=9000)
