from typing import List, Dict, Optional
from src.dao.destination_dao import destination_dao

class DestinationService:
    def add_destination(self, name, country, type_, description) -> Dict:
        return destination_dao.add_destination(name, country, type_, description)

    def list_destinations(self) -> List[Dict]:
        return destination_dao.list_destinations()

    def get_destination(self, dest_id: int) -> Optional[Dict]:
        return destination_dao.get_destination(dest_id)

    def update_destination(self, dest_id: int, fields: Dict) -> Optional[Dict]:
        return destination_dao.update_destination(dest_id, fields)

    def delete_destination(self, dest_id: int) -> Optional[Dict]:
        return destination_dao.delete_destination(dest_id)

destination_service = DestinationService()
