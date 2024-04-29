from flask import jsonify

from scrappy_db.presistance.repository.users_repository import UsersRepository
from scrappy_db.session.user import User


class Users:
    pass


class UsersController:
    users_repository = None

    def __init__(self):
        self.users_repository = UsersRepository()

    def save_user(self, data):
        user = User()
        user.parse_user(data)
        self.users_repository.save_user(user)

        return jsonify({'message': "User {} were added to the database.".format(user.get_login())})
