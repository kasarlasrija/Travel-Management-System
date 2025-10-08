from typing import List, Dict, Optional
from src.config import get_supabase

class DestinationDAO:
    def __init__(self):
        self._client = get_supabase()
        self._table = self._client.table("destinations")

    def add_destination(self, name, country, type_, description) -> Dict:
        self._table.insert({"name": name, "country": country, "type": type_, "description": description}).execute()
        return self._table.select("*").eq("name", name).limit(1).execute().data[0]

    def list_destinations(self) -> List[Dict]:
        return self._table.select("*").execute().data or []

    def get_destination(self, dest_id: int) -> Optional[Dict]:
        resp = self._table.select("*").eq("dest_id", dest_id).limit(1).execute()
        return resp.data[0] if resp.data else None

    def update_destination(self, dest_id: int, fields: Dict) -> Optional[Dict]:
        self._table.update(fields).eq("dest_id", dest_id).execute()
        return self.get_destination(dest_id)

    def delete_destination(self, dest_id: int) -> Optional[Dict]:
        dest = self.get_destination(dest_id)
        if dest:
            self._table.delete().eq("dest_id", dest_id).execute()
        return dest

destination_dao = DestinationDAO()
