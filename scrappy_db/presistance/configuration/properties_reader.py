import configparser


class PropertiesReader:
    # Defining constants
    CONFIG_FILE = "scrappy_db/resources/config.ini"
    DATABASE_CONTEXT = "Database"

    connection_string = None

    config = None

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.CONFIG_FILE)
        self.__database_properties()

    def __database_properties(self):
        self.set_connection_string(self.config.get(self.DATABASE_CONTEXT, "mongodb_connection"))

    def get_connection_string(self):
        return self.connection_string

    def set_connection_string(self, connection_string):
        self.connection_string = connection_string
