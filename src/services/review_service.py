from src.dao.review_dao import review_dao

class ReviewService:
    def __init__(self, dao):
        self._dao = dao

    def add_review(self, user_id: int, package_id: int, rating: int, comment: str):
        return self._dao.add_review(user_id, package_id, rating, comment)

    def list_reviews(self):
        return self._dao.list_reviews()

    def get_reviews_for_package(self, package_id: int):
        return self._dao.get_reviews_for_package(package_id)


# Service instance
review_service = ReviewService(review_dao)
