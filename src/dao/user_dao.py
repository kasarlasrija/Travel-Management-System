from typing import List, Dict, Optional
from src.config import get_supabase

class UserDAO:
    def __init__(self):
        self._client = get_supabase()
        self._table = self._client.table("users")

    def add_user(self, name, email, phone, password, role="Traveler") -> Dict:
        self._table.insert({"name": name, "email": email, "phone": phone, "password": password, "role": role}).execute()
        return self._table.select("*").eq("email", email).limit(1).execute().data[0]

    def list_users(self) -> List[Dict]:
        return self._table.select("*").execute().data or []

    def get_user(self, user_id: int) -> Optional[Dict]:
        resp = self._table.select("*").eq("user_id", user_id).limit(1).execute()
        return resp.data[0] if resp.data else None

    def update_user(self, user_id: int, fields: Dict) -> Optional[Dict]:
        self._table.update(fields).eq("user_id", user_id).execute()
        return self.get_user(user_id)

    def delete_user(self, user_id: int) -> Optional[Dict]:
        user = self.get_user(user_id)
        if user:
            self._table.delete().eq("user_id", user_id).execute()
        return user

user_dao = UserDAO()
