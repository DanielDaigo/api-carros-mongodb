🚗 API de Gerenciamento de Carros (CRUD)
Este projeto é uma aplicação backend para o gerenciamento de uma garagem de veículos, desenvolvida como parte do laboratório de Banco de Dados Não Relacionais. A aplicação utiliza FastAPI para a construção da API e MongoDB como banco de dados NoSQL, rodando em um ambiente conteinerizado com Docker.

🏗️ Arquitetura do Projeto
O projeto segue uma arquitetura modular para garantir a separação de responsabilidades e facilitar a manutenção:

app/routers/: Camada de entrada das requisições HTTP e definição dos endpoints.

app/services/: Contém a lógica de negócio, tratamento de erros e a conexão com o banco de dados.

app/repositories/: Responsável pela comunicação direta e persistência de dados no MongoDB.

app/schemas/: Definição dos modelos de dados (Schemas) utilizando Pydantic para validação.

🛠️ Tecnologias Utilizadas
Python 3.12

FastAPI (Framework Web)

MongoDB (Banco de Dados NoSQL)

Docker & Docker Compose (Containerização)

Pydantic (Validação de Dados)

PyMongo (Driver de conexão MongoDB)

📋 Atributos do Schema (Carro)
Conforme os requisitos da tarefa, o modelo de dados possui 4 atributos principais:

Marca: str

Modelo: str

Ano: int

Cor: str

🚀 Como Rodar o Projeto
1. Clonar o Repositório
Bash
git clone https://github.com/seu-usuario/api-carros-mongodb.git
cd api-carros-mongodb
2. Subir o Banco de Dados (Docker)
A aplicação utiliza um container MongoDB rodando na porta 27019.

Bash
docker-compose up -d
3. Configurar o Ambiente Python
Crie um ambiente virtual e instale as dependências listadas no requirements.txt:

PowerShell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
4. Iniciar a API
Bash
uvicorn main:app --reload
🔌 Endpoints da API
Com a aplicação rodando, você pode acessar a documentação automática (Swagger UI) em:
👉 http://localhost:8000/docs

GET /carros: Lista todos os veículos cadastrados.

POST /carros: Cadastra um novo veículo.

GET /carros/{carro_id}: Busca um veículo específico pelo ID.

PUT /carros/{carro_id}: Atualiza os dados de um veículo existente.

DELETE /carros/{carro_id}: Remove um veículo do sistema.