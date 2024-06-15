import sys

from app.crud import create_user as crud_create_user
from app.database import SessionLocal
from app.schemas import UserCreate


def create_user(username: str, email: str, password: str):
    db = SessionLocal()
    user_create = UserCreate(
        username=username, email=email, password=password
    )
    db_user = crud_create_user(db, user_create)
    db.close()
    return db_user


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: create_user.py <username> <email> <password>")
        sys.exit(1)

    username, email, password = (
        sys.argv[1],
        sys.argv[2],
        sys.argv[3],
    )
    user = create_user(username, email, password)
    print(f"User {user.username} created successfully")
