from src.dao.package_dao import PackageDAO

class PackageService:
    def __init__(self):
        self._dao = PackageDAO()

    def create_package(self, dest_id, name, price, days, details):
        return self._dao.add_package(dest_id, name, price, days, details)

    def list_packages(self):
        return self._dao.list_packages()

    def get_package(self, package_id):
        return self._dao.get_package(package_id)

    def update_package(self, package_id, fields):
        return self._dao.update_package(package_id, fields)

    def delete_package(self, package_id):
        return self._dao.delete_package(package_id)

package_service = PackageService()
