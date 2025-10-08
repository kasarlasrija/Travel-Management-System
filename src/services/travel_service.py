from typing import List, Dict, Optional
from src.dao.travel_dao import travel_dao

class TravelService:
    def create_travel(self, user_id, package_id, day_plan, assistance_notes) -> Dict:
        return travel_dao.create_travel(user_id, package_id, day_plan, assistance_notes)

    def list_travels(self) -> List[Dict]:
        return travel_dao.list_travels()

    def get_travel(self, travel_id: int) -> Optional[Dict]:
        return travel_dao.get_travel(travel_id)

    def update_travel(self, travel_id: int, fields: Dict) -> Optional[Dict]:
        return travel_dao.update_travel(travel_id, fields)

    def delete_travel(self, travel_id: int) -> Optional[Dict]:
        return travel_dao.delete_travel(travel_id)

travel_service = TravelService()
