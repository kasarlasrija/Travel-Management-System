from typing import List, Dict, Optional
from src.config import get_supabase

class BookingDAO:
    def __init__(self):
        self._client = get_supabase()

    def _table(self):
        return self._client.table("bookings")

    def add_booking(self, user_id: int, package_id: int, status: str, total_amount: float) -> Dict:
        payload = {"user_id": user_id, "package_id": package_id, "status": status, "total_amount": total_amount}
        self._table().insert(payload).execute()
        resp = self._table().select("*").order("booking_id", desc=True).limit(1).execute()
        return resp.data[0] if resp.data else None

    def list_bookings(self) -> List[Dict]:
        resp = self._table().select("*").execute()
        return resp.data or []

    def get_booking(self, booking_id: int) -> Optional[Dict]:
        resp = self._table().select("*").eq("booking_id", booking_id).limit(1).execute()
        return resp.data[0] if resp.data else None

    def update_booking(self, booking_id: int, fields: Dict) -> Optional[Dict]:
        self._table().update(fields).eq("booking_id", booking_id).execute()
        return self.get_booking(booking_id)

    def delete_booking(self, booking_id: int) -> Optional[Dict]:
        booking = self.get_booking(booking_id)
        if booking:
            self._table().delete().eq("booking_id", booking_id).execute()
        return booking
