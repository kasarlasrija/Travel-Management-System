from typing import List, Dict, Optional
from src.config import get_supabase

class ReviewDAO:
    def __init__(self):
        self._client = get_supabase()
        self._table = self._client.table("reviews")

    def add_review(self, user_id, package_id, rating, comment) -> Dict:
        self._table.insert({"user_id": user_id, "package_id": package_id, "rating": rating, "comment": comment}).execute()
        return self._table.select("*").eq("user_id", user_id).eq("package_id", package_id).limit(1).execute().data[0]

    def list_reviews(self) -> List[Dict]:
        return self._table.select("*").execute().data or []

    def get_review(self, review_id: int) -> Optional[Dict]:
        resp = self._table.select("*").eq("review_id", review_id).limit(1).execute()
        return resp.data[0] if resp.data else None

    def update_review(self, review_id: int, fields: Dict) -> Optional[Dict]:
        self._table.update(fields).eq("review_id", review_id).execute()
        return self.get_review(review_id)

    def delete_review(self, review_id: int) -> Optional[Dict]:
        r = self.get_review(review_id)
        if r:
            self._table.delete().eq("review_id", review_id).execute()
        return r

review_dao = ReviewDAO()
