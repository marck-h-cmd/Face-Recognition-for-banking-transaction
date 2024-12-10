from pymongo.errors import DuplicateKeyError
from db.database import Database
from datetime import datetime

class Services:
    @staticmethod
    def get_collection():
        return Database.get_db()["services"]
    
    def __init__(self, service_id, client_id, service_type, description, price, date):
        self.service_id = service_id
        self.client_id = client_id
        self.service_type = service_type
        self.description = description
        self.price = price
        self.date = date

    @staticmethod
    def insert(service_id, client_id, service_type, description, price, date):
        collection = Services.get_collection()
        try:
            return collection.insert_one({
                'service_id': service_id,
                'client_id': client_id,
                'service_type': service_type,
                'description': description,
                'price': price,
                'date': date.strftime("%Y-%m-%d")
            })
        except DuplicateKeyError:
            print("Error: Duplicate entry.")
            return None

    @classmethod
    def find_by_service_id(cls, service_id):
        collection = cls.get_collection()
        service_data = collection.find_one({'service_id': service_id})
        return cls(
            service_data['service_id'], service_data['client_id'], 
            service_data['service_type'], service_data['description'],
            service_data['price'], datetime.strptime(service_data['date'], "%Y-%m-%d")
        ) if service_data else None

    @classmethod
    def list_all(cls):
        collection = cls.get_collection()
        services = []
        for service_data in collection.find():
            services.append(cls(
                service_data['service_id'], service_data['client_id'], 
                service_data['service_type'], service_data['description'],
                service_data['price'], datetime.strptime(service_data['date'], "%Y-%m-%d")
            ))
        return services