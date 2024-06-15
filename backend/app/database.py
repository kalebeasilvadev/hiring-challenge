import logging
import os
import time
from dotenv import load_dotenv

from sqlalchemy import create_engine, event
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker
from sqlalchemy_utils import create_database, database_exists

logging_levels = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR,
    "critical": logging.CRITICAL,
}

load_dotenv()

modo = os.getenv("MODO", "info")


DATABASE_URL = os.getenv("DATABASE_URL")

# Configuração de logging
logging.basicConfig(level=logging_levels.get(modo, logging.INFO))
logging.getLogger("sqlalchemy.engine").setLevel(logging_levels.get(modo, logging.INFO))

# Criação do engine com um pool de conexões
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    pool_size=20,  # tamanho do pool de conexões
    max_overflow=0,  # número máximo de conexões extras além do pool_size
)

# Verificar se o banco de dados existe e criar se não existir
if not database_exists(engine.url):
    create_database(engine.url)

# Criação da fábrica de sessões
SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()


# Função para medir o tempo de execução das queries
def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    conn.info.setdefault("query_start_time", []).append(time.time())
    logging.info(f"Start Query: {statement}")


def after_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    total = time.time() - conn.info["query_start_time"].pop(-1)
    logging.info(f"Query Complete! Total Time: {total:.2f} seconds")


# Adicionar listeners para medir tempo de execução das queries
event.listen(engine, "before_cursor_execute", before_cursor_execute)
event.listen(engine, "after_cursor_execute", after_cursor_execute)


# Dependência de banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
