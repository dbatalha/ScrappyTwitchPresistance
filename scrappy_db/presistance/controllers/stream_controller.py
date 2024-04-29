from flask import jsonify
from scrappy_db.presistance.repository.stream_repository import StreamRepository
from scrappy_db.presistance.repository.watch_repository import WatchRepository
from scrappy_db.session.stream import Stream
from scrappy_db.session.watcher import Watcher


class StreamController:
    stream_repository = None
    watch_repository = None

    def __init__(self):
        self.stream_repository = StreamRepository()
        self.watch_repository = WatchRepository()

    def create_stream(self, data):
        watcher = Watcher()
        stream = Stream()
        stream.parse_stream(data)
        watcher.set_name(stream.get_user_name())
        self.watch_repository.add_watcher(watcher)

        self.stream_repository.create_stream(stream, stream.get_user_name())
        return jsonify({'stream': stream.get_user_login(),
                        'message': 'New stream were added successfully.'})

    def get_all_streams(self):
        streams = []
        for stream in self.stream_repository.get_streams():
            streams.append(stream.get("user_name"))

        return jsonify({'streams': streams})

    def update_stream(self, data):
        stream = Stream()
        stream.parse_stream(data)

        self.stream_repository.update_stream(stream.get_stream_id(), stream)
        return jsonify({'stream': stream.get_user_login(),
                        'message': 'Stream were updated successfully'
                        })

    def delete_stream(self, stream_user_name):
        self.stream_repository.delete_stream("user_name", stream_user_name)
        return jsonify({'stream': stream_user_name, '': "The stream {} was deleted.".format(stream_user_name)})
