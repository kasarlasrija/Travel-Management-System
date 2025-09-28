from typing import List, Dict, Optional
from src.config import get_supabase

class PackageDAO:
    def __init__(self):
        self._client = get_supabase()

    def _table(self):
        return self._client.table("packages")

    def add_package(self, dest_id: int, name: str, price: float, days: int, details: str) -> Dict:
        payload = {"dest_id": dest_id, "name": name, "price": price, "days": days, "details": details}
        self._table().insert(payload).execute()
        resp = self._table().select("*").eq("name", name).limit(1).execute()
        return resp.data[0] if resp.data else None

    def list_packages(self) -> List[Dict]:
        resp = self._table().select("*").execute()
        return resp.data or []

    def get_package(self, package_id: int) -> Optional[Dict]:
        resp = self._table().select("*").eq("package_id", package_id).limit(1).execute()
        return resp.data[0] if resp.data else None

    def update_package(self, package_id: int, fields: Dict) -> Optional[Dict]:
        self._table().update(fields).eq("package_id", package_id).execute()
        return self.get_package(package_id)

    def delete_package(self, package_id: int) -> Optional[Dict]:
        pkg = self.get_package(package_id)
        if pkg:
            self._table().delete().eq("package_id", package_id).execute()
        return pkg
