from app.repositories.carro_repository import *
from bson import ObjectId

def format_carro(carro):
    carro["_id"] = str(carro["_id"])
    return carro

def create_carro_service(carro):
    result = create_carro(carro.model_dump())
    return {
        "message": "Carro criado",
        "id": str(result.inserted_id)
    }
    
def get_all_carros_service():
    carros = get_all_carros()
    return [format_carro(carro) for carro in carros]

def get_carro_by_id_service(carro_id):
    try:
        carro = get_carro_by_id(carro_id)
    except:
        return {"error": "Formato de ID invalido"}
    if not carro:
        return {"error": "Carro nao encontrado"}
    return format_carro(carro)

def update_carro_service(carro_id, carro):
    try:
        result = update_carro(carro_id, carro.model_dump())
    except:
        return {"error": "Formato de ID invalido"}
    if result.matched_count == 0:
        return {"error": "Carro nao encontrado"}
    return {"message": "Carro atualizado com sucesso"}

def delete_carro_service(carro_id):
    try:
        result = delete_carro(carro_id)
    except:
        return {"error": "Formato de ID invalido"}
    if result.deleted_count == 0:
        return {"error": "Carro nao encontrado"}
    return {"message": "Carro deletado com sucesso"}