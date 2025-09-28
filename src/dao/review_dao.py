from src.config import get_supabase

class ReviewDAO:
    def __init__(self):
        self._supabase = get_supabase()
        self._table = "reviews"  # make sure your Supabase table is named `reviews`

    def add_review(self, user_id: int, package_id: int, rating: int, comment: str):
        payload = {
            "user_id": int(user_id),
            "package_id": int(package_id),
            "rating": int(rating),
            "comment": comment,
        }
        result = self._supabase.table(self._table).insert(payload).execute()
        return result.data

    def list_reviews(self):
        result = self._supabase.table(self._table).select("*").execute()
        return result.data

    def get_reviews_for_package(self, package_id: int):
        result = (
            self._supabase.table(self._table)
            .select("*")
            .eq("package_id", int(package_id))
            .execute()
        )
        return result.data


# DAO instance
review_dao = ReviewDAO()
