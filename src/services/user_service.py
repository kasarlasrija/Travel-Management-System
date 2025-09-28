from src.dao.user_dao import UserDAO

class UserService:
    def __init__(self):
        self._dao = UserDAO()

    def create_user(self, name, email, phone, password, role="Traveler"):
        return self._dao.add_user(name, email, phone, password, role)

    def get_user(self, user_id):
        return self._dao.get_user(user_id)

    def list_users(self):
        return self._dao.list_users()

    def update_user(self, user_id, fields):
        return self._dao.update_user(user_id, fields)

    def delete_user(self, user_id):
        return self._dao.delete_user(user_id)

user_service = UserService()
