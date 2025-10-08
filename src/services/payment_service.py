from typing import List, Dict, Optional
from src.dao.payment_dao import payment_dao

class PaymentService:
    def make_payment(self, booking_id, amount, status="SUCCESS") -> Dict:
        return payment_dao.make_payment(booking_id, amount, status)

    def list_payments(self) -> List[Dict]:
        return payment_dao.list_payments()

    def get_payment(self, payment_id: int) -> Optional[Dict]:
        return payment_dao.get_payment(payment_id)

    def update_payment(self, payment_id: int, fields: Dict) -> Optional[Dict]:
        return payment_dao.update_payment(payment_id, fields)

    def delete_payment(self, payment_id: int) -> Optional[Dict]:
        return payment_dao.delete_payment(payment_id)

payment_service = PaymentService()
