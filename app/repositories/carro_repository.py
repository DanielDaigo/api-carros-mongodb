from app.services.database import carros_collection
from bson import ObjectId

def create_carro(carro_dict):
    return carros_collection.insert_one(carro_dict)

def get_all_carros():
    return list(carros_collection.find())

def get_carro_by_id(carro_id):
    return carros_collection.find_one({"_id": ObjectId(carro_id)})

def update_carro(carro_id, carro_dict):
    return carros_collection.update_one(
        {"_id": ObjectId(carro_id)},
        {"$set": carro_dict}
    )

def delete_carro(carro_id):
    return carros_collection.delete_one({"_id": ObjectId(carro_id)})