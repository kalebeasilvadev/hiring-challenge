from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import auth, csv_upload, history, user
from app.timing_middleware import TimingMiddleware
from app.utils import get_current_user

app = FastAPI()

origins = [
    "http://localhost:8888",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(TimingMiddleware)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(
    csv_upload.router,
    prefix="/csv",
    tags=["csv"],
    dependencies=[Depends(get_current_user)],
)
app.include_router(
    history.router,
    prefix="/history",
    tags=["history"],
    dependencies=[Depends(get_current_user)],
)
app.include_router(
    user.router,
    prefix="/user",
    tags=["user"],
    dependencies=[Depends(get_current_user)],
)
