from flask import Blueprint, jsonify, abort, request
from scrappy_db.presistance.controllers.stream_controller import StreamController
from scrappy_db.presistance.controllers.users_controller import UsersController
from scrappy_db.presistance.controllers.watch_controller import WatchController

main = Blueprint('main', __name__)
stream_controller = StreamController()
watch_controller = WatchController()
users_controller = UsersController()


@main.route('/')
def index():
    return jsonify({"message": "Welcome to the Scrappy DB app!"})


@main.route('/stream', methods=['POST'])
def create_stream():
    return stream_controller.create_stream(request.json)


@main.route('/stream', methods=['PUT'])
def update_stream():
    return stream_controller.update_stream(request.json)


@main.route('/stream', methods=['DELETE'])
def delete_stream():
    return stream_controller.delete_stream(request.args.get('user_name'))


@main.route('/streams', methods=['GET'])
def get_streams():
    return stream_controller.get_all_streams()


@main.route('/watchers', methods=['GET'])
def get_all_watchers():
    return watch_controller.get_all_watchers()


@main.route('/watcher', methods=['POST'])
def add_watcher():
    return watch_controller.add_watcher(request.json)


@main.route('/user', methods=['POST'])
def save_user():
    return users_controller.save_user(request.json)


@main.route('/bad_request')
def bad_request():
    abort(400)


@main.route('/server_error')
def server_error():
    abort(500)
