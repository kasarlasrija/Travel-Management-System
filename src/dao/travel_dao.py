from typing import List, Dict, Optional
from src.config import get_supabase

class TravelDAO:
    def __init__(self):
        self._client = get_supabase()
        self._table = self._client.table("travels")

    def create_travel(self, user_id, package_id, day_plan, assistance_notes) -> Dict:
        self._table.insert({"user_id": user_id, "package_id": package_id, "day_plan": day_plan, "assistance_notes": assistance_notes}).execute()
        return self._table.select("*").eq("user_id", user_id).eq("package_id", package_id).limit(1).execute().data[0]

    def list_travels(self) -> List[Dict]:
        return self._table.select("*").execute().data or []

    def get_travel(self, travel_id: int) -> Optional[Dict]:
        resp = self._table.select("*").eq("travel_id", travel_id).limit(1).execute()
        return resp.data[0] if resp.data else None

    def update_travel(self, travel_id: int, fields: Dict) -> Optional[Dict]:
        self._table.update(fields).eq("travel_id", travel_id).execute()
        return self.get_travel(travel_id)

    def delete_travel(self, travel_id: int) -> Optional[Dict]:
        t = self.get_travel(travel_id)
        if t:
            self._table.delete().eq("travel_id", travel_id).execute()
        return t

travel_dao = TravelDAO()
