from src.dao.destination_dao import DestinationDAO

class DestinationService:
    def __init__(self):
        self._dao = DestinationDAO()

    def create_destination(self, name, country, type_, description):
        return self._dao.add_destination(name, country, type_, description)

    def list_destinations(self):
        return self._dao.list_destinations()

    def get_destination(self, dest_id):
        return self._dao.get_destination(dest_id)

    def update_destination(self, dest_id, fields):
        return self._dao.update_destination(dest_id, fields)

    def delete_destination(self, dest_id):
        return self._dao.delete_destination(dest_id)

destination_service = DestinationService()
