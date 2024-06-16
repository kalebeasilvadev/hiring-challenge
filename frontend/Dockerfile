# Dockerfile
FROM node:20

# Instalar Bun
RUN npm install -g bun

WORKDIR /app

# Copiar e instalar dependências com Bun
COPY package*.json ./
RUN bun install

# Copiar o restante do código
COPY . .

# Expor a porta e iniciar a aplicação com Bun
EXPOSE 3000
CMD ["bun","run", "dev"]
