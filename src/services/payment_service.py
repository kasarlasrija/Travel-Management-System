from src.dao.payment_dao import PaymentDAO

class PaymentService:
    def __init__(self):
        self._dao = PaymentDAO()

    def make_payment(self, booking_id, amount, status):
        return self._dao.add_payment(booking_id, amount, status)

    def list_payments(self):
        return self._dao.list_payments()

    def get_payment(self, payment_id):
        return self._dao.get_payment(payment_id)

    def update_payment(self, payment_id, fields):
        return self._dao.update_payment(payment_id, fields)

    def delete_payment(self, payment_id):
        return self._dao.delete_payment(payment_id)

payment_service = PaymentService()
