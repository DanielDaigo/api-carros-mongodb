from pydantic import BaseModel

class Carro(BaseModel):
    marca: str
    modelo: str
    ano: int
    cor: str