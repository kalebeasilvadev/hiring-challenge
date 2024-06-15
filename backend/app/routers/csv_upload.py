from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from .. import schemas, crud
from ..database import get_db
import pandas as pd
import os
import tempfile
from datetime import datetime

router = APIRouter()


@router.post("/uploadfile/", response_model=schemas.FileUpload)
async def create_upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    dt_inicio = datetime.now()
    content = await file.read()

    # Cria um arquivo temporário
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(content)
    temp_file.close()

    # Agora podemos ler o arquivo com pandas
    df = pd.read_csv(temp_file.name)
    print(f"tempo de execução: {datetime.now() - dt_inicio}")

    file_upload = schemas.FileUploadCreate(
        filename=file.filename,
        size=len(content),
        rows=len(df)
    )

    # Remove o arquivo temporário
    os.unlink(temp_file.name)

    return crud.create_file_upload(db=db, file_upload=file_upload)
