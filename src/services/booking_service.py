from src.dao.booking_dao import BookingDAO

class BookingService:
    def __init__(self):
        self._dao = BookingDAO()

    def create_booking(self, user_id, package_id, status, total_amount):
        return self._dao.add_booking(user_id, package_id, status, total_amount)

    def list_bookings(self):
        return self._dao.list_bookings()

    def get_booking(self, booking_id):
        return self._dao.get_booking(booking_id)

    def update_booking(self, booking_id, fields):
        return self._dao.update_booking(booking_id, fields)

    def delete_booking(self, booking_id):
        return self._dao.delete_booking(booking_id)

booking_service = BookingService()
