from typing import List, Dict, Optional
from src.dao.user_dao import user_dao

class UserService:
    def add_user(self, name, email, phone, password, role="Traveler") -> Dict:
        return user_dao.add_user(name, email, phone, password, role)

    def list_users(self) -> List[Dict]:
        return user_dao.list_users()

    def get_user(self, user_id: int) -> Optional[Dict]:
        return user_dao.get_user(user_id)

    def update_user(self, user_id: int, fields: Dict) -> Optional[Dict]:
        return user_dao.update_user(user_id, fields)

    def delete_user(self, user_id: int) -> Optional[Dict]:
        return user_dao.delete_user(user_id)

user_service = UserService()
