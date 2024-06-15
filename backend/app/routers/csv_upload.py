import tempfile
import threading

import pandas as pd
from fastapi import APIRouter, BackgroundTasks, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db
from app.models import ProcessingHistory
from app.services.processing_csv import process_csv

router = APIRouter()


@router.post("/uploadfile/")
async def create_upload_file(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    content = await file.read()

    # Cria um arquivo temporário
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(content)
    temp_file.close()

    # Agora podemos ler o arquivo com pandas
    df = pd.read_csv(temp_file.name)

    # Criar entrada no histórico com status "pendente"
    history_entry = ProcessingHistory(status="pendente", size=len(df))
    db.add(history_entry)
    db.commit()
    db.refresh(history_entry)

    # Adicionar tarefa em background para processar o CSV
    background_tasks.add_task(
        threading.Thread(
            target=process_csv, args=(temp_file.name, db, history_entry.id)
        ).start
    )

    file_upload = schemas.FileUploadCreate(
        filename=file.filename,
        size=len(content),
        rows=len(df),
        history_id=history_entry.id,
    )

    return crud.create_file_upload(db=db, file_upload=file_upload)
