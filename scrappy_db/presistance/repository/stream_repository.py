from scrappy_db.presistance.configuration.mongodb_client import MongoDBClient
from scrappy_db.presistance.configuration.properties_reader import PropertiesReader


class StreamRepository:
    STREAMS = "Streams"
    DATABASE = "Scrappy"

    mongodb_client = None
    properties = None

    def __init__(self):
        self.properties = PropertiesReader()

    def __stream_setup(self):
        self.mongodb_client.set_database(self.DATABASE)
        self.mongodb_client.set_collection(self.STREAMS)

    def __setup(self):
        self.mongodb_client = MongoDBClient(self.properties.get_connection_string())

    def create_stream(self, stream, stream_name):
        self.__setup()
        self.__stream_setup()

        found_document = self.mongodb_client.find_one_element("_id", stream.get_id())
        if found_document:
            self.update_stream(stream.get_id(), stream)
        else:
            self.mongodb_client.insert_one_collection(stream)

        self.__close()

    def get_streams(self):
        self.__setup()
        self.__stream_setup()

        return self.mongodb_client.find_all()

    def update_stream(self, qfilter, stream):
        self.__setup()
        self.__stream_setup()

        query_filter = {'_id': qfilter}
        update_data = {'$set': stream.__dict__}

        self.mongodb_client.update_one_collection(query_filter, update_data)
        self.__close()

    def delete_stream(self, key, value):
        self.__setup()
        self.__stream_setup()

        self.mongodb_client.delete_many(key, value)
        self.__close()

    def __close(self):
        self.mongodb_client.close()
