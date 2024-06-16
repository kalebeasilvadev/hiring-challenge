FROM python:3.10-rc-slim-buster

WORKDIR /app

# Copiar e instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código
COPY . .

# Executar migrações e criar usuário admin no ponto de entrada
CMD ["sh", "-c", "alembic upgrade head && python create_user.py --username admin --password admin --email admin@admin"]

# Expor a porta
EXPOSE 8050
