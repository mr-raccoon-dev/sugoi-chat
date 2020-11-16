from fastapi import APIRouter

from .endpoints import users, auth

router = APIRouter()

router.include_router(auth.router, prefix="/auth", tags=["users"])
router.include_router(users.router, prefix="/users", tags=["users"])
