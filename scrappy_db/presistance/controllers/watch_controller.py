from flask import Flask, request, jsonify
from scrappy_db.presistance.repository.watch_repository import WatchRepository
from scrappy_db.session.watcher import Watcher


class WatchController:
    watch_repository = None

    def __init__(self):
        self.watch_repository = WatchRepository()

    def get_all_watchers(self):
        watchers = []
        for watch in self.watch_repository.get_all_watchers():
            watchers.append(watch.get("name"))

        return jsonify({'watchers': watchers})

    def add_watcher(self, data):
        watcher = Watcher()
        watcher.parse_watcher(data)
        self.watch_repository.add_watcher(watcher)

        return jsonify({'message': "Streamer {} were added to the watch list.".format(watcher.get_name())})
