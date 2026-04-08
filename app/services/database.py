from pymongo import MongoClient

# Apontando para a nova porta definida no compose.yaml
MONGO_URL = "mongodb://localhost:27019/"

client = MongoClient(MONGO_URL)

# Criando um novo banco de dados
db = client["garagem_db"]

# Criando a nova collection
carros_collection = db["carros"]