from typing import List, Dict, Optional
from src.config import get_supabase

class PaymentDAO:
    def __init__(self):
        self._client = get_supabase()

    def _table(self):
        return self._client.table("payments")

    def add_payment(self, booking_id: int, amount: float, status: str) -> Dict:
        payload = {"booking_id": booking_id, "amount": amount, "status": status}
        self._table().insert(payload).execute()
        resp = self._table().select("*").eq("booking_id", booking_id).order("payment_id", desc=True).limit(1).execute()
        return resp.data[0] if resp.data else None

    def list_payments(self) -> List[Dict]:
        resp = self._table().select("*").execute()
        return resp.data or []

    def get_payment(self, payment_id: int) -> Optional[Dict]:
        resp = self._table().select("*").eq("payment_id", payment_id).limit(1).execute()
        return resp.data[0] if resp.data else None

    def update_payment(self, payment_id: int, fields: Dict) -> Optional[Dict]:
        self._table().update(fields).eq("payment_id", payment_id).execute()
        return self.get_payment(payment_id)

    def delete_payment(self, payment_id: int) -> Optional[Dict]:
        payment = self.get_payment(payment_id)
        if payment:
            self._table().delete().eq("payment_id", payment_id).execute()
        return payment
