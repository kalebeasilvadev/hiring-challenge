import datetime

from sqlalchemy import Boolean, Column, DateTime, Integer, String

from app.database import Base


class FileUpload(Base):
    __tablename__ = "file_uploads"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    size = Column(Integer)
    rows = Column(Integer)
    upload_time = Column(DateTime, default=datetime.datetime.utcnow)
    history_id = Column(Integer, index=True)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)


class ProcessingHistory(Base):
    __tablename__ = "processing_history"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, index=True)
    success_count = Column(Integer, default=0)
    failure_count = Column(Integer, default=0)
    size = Column(Integer)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)
