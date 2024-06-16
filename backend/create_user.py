import argparse

from app.crud import create_user as crud_create_user, get_user_by_username
from app.database import SessionLocal
from app.schemas import UserCreate


def create_user(username: str, email: str, password: str):
    db = SessionLocal()
    if get_user_by_username(db, username):
        return False
    user_create = UserCreate(username=username, email=email, password=password)
    db_user = crud_create_user(db, user_create)
    db.close()
    return db_user


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create a new user.")
    parser.add_argument("--username", required=True, help="Username for the new user.")
    parser.add_argument("--email", required=True, help="Email for the new user.")
    parser.add_argument("--password", required=True, help="Password for the new user.")

    args = parser.parse_args()

    user = create_user(args.username, args.email, args.password)
    if not user:
        print(f"User {args.username} already exists")
    else:
        print(f"User {user.username} created successfully")
