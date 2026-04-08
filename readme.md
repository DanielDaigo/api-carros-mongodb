# API de Carros com MongoDB

API REST para cadastro e gerenciamento de carros, desenvolvida com FastAPI e MongoDB.

## Objetivo

Este projeto implementa um CRUD completo para carros com arquitetura modular, separando:

- roteamento
- regra de negocio
- acesso a dados
- validacao de schema

## Stack

- Python
- FastAPI
- MongoDB
- PyMongo
- Docker Compose

## Estrutura do Projeto

```text
.
├── compose.yaml
├── main.py
├── requirements.txt
└── app
		├── repositories
		│   └── carro_repository.py
		├── routers
		│   └── carro_router.py
		├── schemas
		│   └── carro_schema.py
		└── services
				├── carro_service.py
				└── database.py
```

## Modelo de Dados

O schema `Carro` possui os campos:

- `marca` (string)
- `modelo` (string)
- `ano` (inteiro)
- `cor` (string)

Exemplo de payload:

```json
{
  "marca": "Toyota",
  "modelo": "Corolla",
  "ano": 2022,
  "cor": "Prata"
}
```

## Como Executar

### 1. Clonar o repositorio

```bash
git clone https://github.com/DanielDaigo/api-carros-mongodb.git
cd api-carros-mongodb
```

### 2. Subir o MongoDB com Docker

```bash
docker compose up -d
```

O MongoDB sera exposto localmente em `localhost:27019`.

### 3. Criar e ativar ambiente virtual

No Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Rodar a API

```bash
uvicorn main:app --reload
```

API disponivel em:

- `http://127.0.0.1:8000`
- Swagger UI: `http://127.0.0.1:8000/docs`

## Endpoints

Base URL: `http://127.0.0.1:8000`

### `GET /`

Retorna mensagem de status da API.

Resposta:

```json
{
  "message": "API de Carros Modular rodando com sucesso!"
}
```

### `GET /carros`

Lista todos os carros cadastrados.

### `POST /carros`

Cria um novo carro.

Corpo esperado:

```json
{
  "marca": "Honda",
  "modelo": "Civic",
  "ano": 2021,
  "cor": "Preto"
}
```

Resposta de sucesso:

```json
{
  "message": "Carro criado",
  "id": "<id_gerado>"
}
```

### `GET /carros/{carro_id}`

Busca um carro pelo ID.

Possiveis respostas de erro:

```json
{
  "error": "Formato de ID invalido"
}
```

```json
{
  "error": "Carro nao encontrado"
}
```

### `PUT /carros/{carro_id}`

Atualiza um carro existente pelo ID.

Resposta de sucesso:

```json
{
  "message": "Carro atualizado com sucesso"
}
```

### `DELETE /carros/{carro_id}`

Remove um carro pelo ID.

Resposta de sucesso:

```json
{
  "message": "Carro deletado com sucesso"
}
```

## Observacoes

- A conexao com MongoDB esta definida em `app/services/database.py` usando a URL `mongodb://localhost:27019/`.
- O banco utilizado e `garagem_db` e a collection e `carros`.
- As validacoes de entrada sao feitas com Pydantic via schema `Carro`.
