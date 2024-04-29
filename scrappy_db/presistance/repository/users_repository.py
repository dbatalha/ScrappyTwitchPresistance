from scrappy_db.presistance.configuration.mongodb_client import MongoDBClient
from scrappy_db.presistance.configuration.properties_reader import PropertiesReader


class UsersRepository:
    USERS = "Users"
    DATABASE = "Scrappy"

    mongodb_client = None

    def __init__(self):
        properties = PropertiesReader()
        self.mongodb_client = MongoDBClient(properties.get_connection_string())

    def __users_setup(self):
        self.mongodb_client.set_database(self.DATABASE)
        self.mongodb_client.set_collection(self.USERS)

    def save_user(self, user):
        self.__users_setup()

        found_document = self.mongodb_client.find_one_element("_id", user.get_user_id())
        if found_document:
            pass
        else:
            self.mongodb_client.insert_one_collection(user)
