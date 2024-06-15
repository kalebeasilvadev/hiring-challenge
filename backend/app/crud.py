from sqlalchemy.orm import Session

from app import models, schemas
from app.utils import get_password_hash


def create_file_upload(db: Session, file_upload: schemas.FileUploadCreate):
    db_file_upload = models.FileUpload(**file_upload.dict())
    db.add(db_file_upload)
    db.commit()
    db.refresh(db_file_upload)
    return db_file_upload


def get_file_uploads(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.FileUpload).offset(skip).limit(limit).all()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_processing_history(db: Session, id: int):
    return (
        db.query(models.ProcessingHistory)
        .filter(models.ProcessingHistory.id == id)
        .first()
    )
