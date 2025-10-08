from typing import List, Dict, Optional
from src.dao.booking_dao import booking_dao

class BookingService:
    def create_booking(self, user_id, package_id, status="PLACED", total_amount=0.0) -> Dict:
        return booking_dao.create_booking(user_id, package_id, status, total_amount)

    def list_bookings(self) -> List[Dict]:
        return booking_dao.list_bookings()

    def get_booking(self, booking_id: int) -> Optional[Dict]:
        return booking_dao.get_booking(booking_id)

    def update_booking(self, booking_id: int, fields: Dict) -> Optional[Dict]:
        return booking_dao.update_booking(booking_id, fields)

    def delete_booking(self, booking_id: int) -> Optional[Dict]:
        return booking_dao.delete_booking(booking_id)

booking_service = BookingService()
