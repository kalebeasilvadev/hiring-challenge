import os

import pandas as pd
from sqlalchemy.orm import Session

from app.models import ProcessingHistory


def process_csv(file_path: str, db: Session, history_id: int):
    # Definir variáveis de contagem
    success_count = 0
    failure_count = 0
    qty_processed = 0
    chunksize = int(os.getenv("CSV_CHUNKSIZE", 1000))

    # Ler o arquivo CSV em chunks
    chunk_iter = pd.read_csv(file_path, chunksize=chunksize, iterator=True)

    for chunk in chunk_iter:
        # Processar cada linha do chunk
        for _, row in chunk.iterrows():
            if validate_csv_row(row):
                simulate_email_sending(row["email"], row["debtId"])
                success_count += 1
            else:
                failure_count += 1
        qty_processed += len(chunk)

        # Atualizar o banco de dados após cada chunk
        update_processing_status(db, history_id, "em progresso", success_count, failure_count)

    # Remover o arquivo CSV
    os.unlink(file_path)

    # Atualizar o status final do processamento
    update_processing_status(db, history_id, "concluído", success_count, failure_count)


def validate_csv_row(row) -> bool:
    # Implementar validação dos campos do CSV
    required_columns = [
        "name",
        "governmentId",
        "email",
        "debtAmount",
        "debtDueDate",
        "debtId",
    ]
    for col in required_columns:
        if pd.isna(row[col]):
            return False
    # Adicionar mais validações conforme necessário
    return True


def simulate_email_sending(email: str, debt_id: str):
    # Simulação do envio de e-mail
    print(f"Simulando envio de e-mail para {email} com o boleto {debt_id}")


def update_processing_status(
    db: Session,
    history_id: int,
    status: str,
    success_count: int = 0,
    failure_count: int = 0,
):
    # Atualizar status do histórico de processamento
    history_entry = (
        db.query(ProcessingHistory).filter(ProcessingHistory.id == history_id).first()
    )
    if history_entry:
        history_entry.status = status
        history_entry.success_count = success_count
        history_entry.failure_count = failure_count
        db.commit()
