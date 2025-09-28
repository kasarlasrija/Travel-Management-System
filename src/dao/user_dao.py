from typing import List, Dict, Optional
from src.config import get_supabase

class UserDAO:
    def __init__(self):
        self._client = get_supabase()

    def _table(self):
        return self._client.table("users")

    def add_user(self, name: str, email: str, phone: str, password: str, role: str = "Traveler") -> Dict:
        payload = {"name": name, "email": email, "phone": phone, "password": password, "role": role}
        self._table().insert(payload).execute()
        resp = self._table().select("*").eq("email", email).limit(1).execute()
        return resp.data[0] if resp.data else None

    def get_user(self, user_id: int) -> Optional[Dict]:
        resp = self._table().select("*").eq("user_id", user_id).limit(1).execute()
        return resp.data[0] if resp.data else None

    def list_users(self) -> List[Dict]:
        resp = self._table().select("*").execute()
        return resp.data or []

    def update_user(self, user_id: int, fields: Dict) -> Optional[Dict]:
        self._table().update(fields).eq("user_id", user_id).execute()
        return self.get_user(user_id)

    def delete_user(self, user_id: int) -> Optional[Dict]:
        user = self.get_user(user_id)
        if user:
            self._table().delete().eq("user_id", user_id).execute()
        return user
