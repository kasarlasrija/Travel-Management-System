from src.dao.travel_dao import TravelDAO

class TravelService:
    def __init__(self):
        self._dao = TravelDAO()

    def create_travel(self, user_id, package_id, day_plan, assistance_notes=""):
        return self._dao.add_travel(user_id, package_id, day_plan, assistance_notes)

    def list_travels(self):
        return self._dao.list_travels()

    def get_travel(self, travel_id):
        return self._dao.get_travel(travel_id)

    def update_travel(self, travel_id, fields):
        return self._dao.update_travel(travel_id, fields)

    def delete_travel(self, travel_id):
        return self._dao.delete_travel(travel_id)

travel_service = TravelService()
