### Resumo do Projeto

Este projeto é um desafio técnico que envolve o desenvolvimento de um backend responsável por receber e processar arquivos CSV, além de manter um histórico das importações realizadas. O sistema deve validar a estrutura dos dados, simular o envio de e-mails com boletos de pagamento, registrar erros no histórico em caso de falhas de validação e manter o status de processamento (pendente, em progresso ou concluído). O processamento dos dados deve ser executado em uma thread separada e, após a conclusão, o histórico deve ser atualizado.

### Tecnologias Utilizadas

#### Backend
- **Linguagens de Programação:** Python
- **Frameworks e Bibliotecas:**
  - FastAPI
  - SQLAlchemy
  - Alembic
  - Pandas
  - Pydantic
  - Pytest
- **Banco de Dados:** SQLite
- **Ferramentas e Tecnologias:**
  - Docker
  - Git
- **Outras Tecnologias:**
  - API RESTful
  - Validação de Dados

#### Frontend
- **Linguagens de Programação:** JavaScript, TypeScript
- **Frameworks e Bibliotecas:**
  - React
  - Axios
  - tailwindcss
  - react-router-dom
- **Ferramentas e Tecnologias:**
  - Vite
  - Bun

### Arquivo .env Necessário

Para o correto funcionamento do projeto, é necessário criar um arquivo `.env` na raiz do projeto com as seguintes variáveis de ambiente:

```env
DATABASE_URL=sqlite:///db/sql_app.db
SECRET_KEY=s3nh@_ultr4_s3cr3t@
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
MODO=info
CSV_CHUNKSIZE=100000
```

Estas variáveis configuram a URL do banco de dados, a chave secreta para geração de tokens, o algoritmo de criptografia, o tempo de expiração dos tokens, o modo de execução da aplicação e o tamanho dos chunks de leitura dos arquivos CSV.

### Como Executar o Projeto

1. Clone o repositório:
   ```sh
   git clone https://github.com/kalebeasilvadev/hiring-challenge.git
   ```

2. Navegue até o diretório do projeto:
   ```sh
   cd hiring-challenge
   ```

3. Crie e configure o arquivo `.env` conforme indicado acima.

4. Instale as dependências do projeto:
   ```sh
   python -m venv venv
   source venv/bin/activate # Linux
   venv\Scripts\activate # Windows  
   pip install -r requirements.txt
   ```

5. Execute as migrações para configurar o banco de dados:
   ```sh
   alembic upgrade head
   ```

6. Inicie a aplicação:
   ```sh
   python backend/main.py
   ```
   ou
   ```sh
    python main.py
    ```
7. Para teste Unitário:
   ```sh
   pytest backend/tests
   ```


A aplicação estará disponível em `http://127.0.0.1:8000`.

usuario padrão: admin senha: admin

### Funcionalidades

- **Recebimento de Arquivos CSV:** Endpoint para upload de arquivos CSV contendo informações de dívidas.
- **Validação de Dados:** Verificação da estrutura dos dados no arquivo CSV.
- **Simulação de Envio de E-mails:** Simulação do envio de boletos de pagamento via e-mail.
- **Histórico de Importações:** Registro de todas as importações realizadas, incluindo erros e status de processamento.