from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app import crud, database, schemas
from app.utils import create_access_token, verify_password

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

router = APIRouter()


class LoginData(BaseModel):
    username: str
    password: str


@router.post("/token", response_model=schemas.Token)
async def login_for_access_token(
    request: Request, db: Session = Depends(database.get_db)
):
    if request.headers.get("content-type") == "application/x-www-form-urlencoded":
        form_data = await request.form()
        username = form_data["username"]
        password = form_data["password"]
    else:
        json_data = await request.json()
        username = json_data["username"]
        password = json_data["password"]

    user = authenticate_user(db, username, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


def authenticate_user(db, username: str, password: str):
    user = crud.get_user_by_username(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user
