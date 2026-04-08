from fastapi import APIRouter
from app.schemas.carro_schema import Carro
from app.services.carro_service import *

router = APIRouter()

# GET /All carros
@router.get("/carros")
def list_carros():
    return get_all_carros_service()

# POST - CREATE CARRO
@router.post("/carros")
def create_carro(carro: Carro):
    return create_carro_service(carro)

# GET - CARRO BY ID
@router.get("/carros/{carro_id}")
def get_carro(carro_id: str):
    return get_carro_by_id_service(carro_id)

# UPDATE
@router.put("/carros/{carro_id}")
def update_carro(carro_id: str, carro: Carro):
    return update_carro_service(carro_id, carro)

# DELETE
@router.delete("/carros/{carro_id}")
def delete_carro(carro_id: str):
    return delete_carro_service(carro_id)