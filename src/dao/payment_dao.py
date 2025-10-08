from typing import List, Dict, Optional
from src.config import get_supabase

class PaymentDAO:
    def __init__(self):
        self._client = get_supabase()
        self._table = self._client.table("payments")

    def make_payment(self, booking_id, amount, status="SUCCESS") -> Dict:
        self._table.insert({"booking_id": booking_id, "amount": amount, "status": status}).execute()
        return self._table.select("*").eq("booking_id", booking_id).limit(1).execute().data[0]

    def list_payments(self) -> List[Dict]:
        return self._table.select("*").execute().data or []

    def get_payment(self, payment_id: int) -> Optional[Dict]:
        resp = self._table.select("*").eq("payment_id", payment_id).limit(1).execute()
        return resp.data[0] if resp.data else None

    def update_payment(self, payment_id: int, fields: Dict) -> Optional[Dict]:
        self._table.update(fields).eq("payment_id", payment_id).execute()
        return self.get_payment(payment_id)

    def delete_payment(self, payment_id: int) -> Optional[Dict]:
        p = self.get_payment(payment_id)
        if p:
            self._table.delete().eq("payment_id", payment_id).execute()
        return p

payment_dao = PaymentDAO()
