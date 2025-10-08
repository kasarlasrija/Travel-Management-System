from typing import List, Dict, Optional
from src.dao.review_dao import review_dao

class ReviewService:
    def add_review(self, user_id, package_id, rating, comment) -> Dict:
        return review_dao.add_review(user_id, package_id, rating, comment)

    def list_reviews(self) -> List[Dict]:
        return review_dao.list_reviews()

    def get_review(self, review_id: int) -> Optional[Dict]:
        return review_dao.get_review(review_id)

    def update_review(self, review_id: int, fields: Dict) -> Optional[Dict]:
        return review_dao.update_review(review_id, fields)

    def delete_review(self, review_id: int) -> Optional[Dict]:
        return review_dao.delete_review(review_id)

review_service = ReviewService()
