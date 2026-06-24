TaskMaster API

## Visão Geral
O **TaskMaster API** é uma solução de backend focada em performance e organização. O objetivo deste projeto foi construir uma API RESTful completa para gerenciamento de tarefas, seguindo padrões de mercado como injeção de dependência e separação de camadas.

---

## Arquitetura do Projeto
O projeto foi estruturado para ser escalável e de fácil manutenção, utilizando a seguinte separação:
- **`app/main.py`**: Ponto de entrada da aplicação e definição das rotas.
- **`app/models.py`**: Modelagem das tabelas no banco de dados com SQLAlchemy.
- **`app/schemas.py`**: Definição dos contratos de dados (Pydantic) para validação de entrada/saída.
- **`app/database.py`**: Configuração da conexão com o banco de dados.

##  Estrutura de Pastas
```text
taskmaster-api/
├── app/
│   ├── database.py    # Configurações do SQLAlchemy
│   ├── main.py        # Rotas e lógica da API
│   ├── models.py      # Definição das tabelas (ORM)
│   └── schemas.py     # Validação de dados (Pydantic)
├── requirements.txt   # Dependências do projeto
└── README.md          # Documentação oficial

Tecnologias Utilizadas
Linguagem: Python 3.10+

Framework: FastAPI (Alta performance, suporte assíncrono e auto-documentação)

Banco de Dados: SQLite (Persistência local)

ORM: SQLAlchemy (Mapeamento Objeto-Relacional)

Validação: Pydantic v2 (Modelagem de dados)

Como Executar Localmente
Siga os passos abaixo para ter o projeto rodando em sua máquina:

Clone o repositório:
git clone https://github.com/RAHZ05/taskmaster-api.git

Crie o ambiente virtual:
python -m venv venv

Ative o ambiente:
venv\\Scripts\\activate (Windows) ou source venv/bin/activate (Linux/Mac)

Instale as dependências:
pip install -r requirements.txt

Execute a API:
python -m uvicorn app.main:app --reload

Acesse:
Abra seu navegador em http://127.0.0.1:8000/docs

Roadmap (Melhorias Futuras)
O projeto está em constante evolução. Futuras implementações incluirão:

[ ] Autenticação via JWT (Login seguro).

[ ] Rotas de PATCH e DELETE para edição e exclusão de tarefas.

[ ] Dockerização para deploy facilitado.

[ ] Testes unitários utilizando pytest.

 Demonstração da API

Abaixo, algumas capturas de tela do funcionamento da API através da documentação interativa (Swagger 

<img src="https://github.com/user-attachments/assets/b78f7b5e-4c6f-4c7f-bc1a-134bdd2d770c" width="400" height="400" alt="Captura de tela">













Desenvolvido por Raquel Alves.
"""
#Python #FastAPI #Backend #SQLAlchemy #Portfolio
