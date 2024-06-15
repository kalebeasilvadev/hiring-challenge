from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class FileUploadBase(BaseModel):
    filename: str
    size: int
    rows: int


class FileUploadCreate(FileUploadBase):
    pass


class FileUpload(FileUploadBase):
    id: int
    upload_time: datetime = datetime.now()

    model_config = ConfigDict(
        from_attributes=True
    )


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None


class UserBase(BaseModel):
    username: str
    email: str
    is_active: Optional[bool] = True


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    model_config = ConfigDict(
        from_attributes=True
    )


class UserInDB(User):
    hashed_password: str
