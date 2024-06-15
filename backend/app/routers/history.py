from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter()


@router.get("/uploads/", response_model=list[schemas.FileUpload])
def read_uploads(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    uploads = crud.get_file_uploads(db, skip=skip, limit=limit)
    return uploads


@router.get("/processing/", response_model=schemas.ProcessingHistoryBase)
def read_processing_history(id: int, db: Session = Depends(get_db)):
    return crud.get_processing_history(db, id=id)
