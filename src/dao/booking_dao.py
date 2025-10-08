from typing import List, Dict, Optional
from src.config import get_supabase

class BookingDAO:
    def __init__(self):
        self._client = get_supabase()
        self._table = self._client.table("bookings")

    def create_booking(self, user_id, package_id, status="PLACED", total_amount=0.0) -> Dict:
        self._table.insert({"user_id": user_id, "package_id": package_id, "status": status, "total_amount": total_amount}).execute()
        return self._table.select("*").eq("user_id", user_id).eq("package_id", package_id).limit(1).execute().data[0]

    def list_bookings(self) -> List[Dict]:
        return self._table.select("*").execute().data or []

    def get_booking(self, booking_id: int) -> Optional[Dict]:
        resp = self._table.select("*").eq("booking_id", booking_id).limit(1).execute()
        return resp.data[0] if resp.data else None

    def update_booking(self, booking_id: int, fields: Dict) -> Optional[Dict]:
        self._table.update(fields).eq("booking_id", booking_id).execute()
        return self.get_booking(booking_id)

    def delete_booking(self, booking_id: int) -> Optional[Dict]:
        booking = self.get_booking(booking_id)
        if booking:
            self._table.delete().eq("booking_id", booking_id).execute()
        return booking

booking_dao = BookingDAO()
