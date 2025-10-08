from typing import List, Dict, Optional
from src.dao.package_dao import package_dao

class PackageService:
    def add_package(self, dest_id, name, price, days, details) -> Dict:
        return package_dao.add_package(dest_id, name, price, days, details)

    def list_packages(self) -> List[Dict]:
        return package_dao.list_packages()

    def get_package(self, package_id: int) -> Optional[Dict]:
        return package_dao.get_package(package_id)

    def update_package(self, package_id: int, fields: Dict) -> Optional[Dict]:
        return package_dao.update_package(package_id, fields)

    def delete_package(self, package_id: int) -> Optional[Dict]:
        return package_dao.delete_package(package_id)

package_service = PackageService()
