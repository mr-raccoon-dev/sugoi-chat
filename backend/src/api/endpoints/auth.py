from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import APIKeyHeader

from api.deps.auth import get_current_user
from api.schemas.users import AuthUser, Token, User_Pydantic
from auth.services import AuthService

router = APIRouter()
auth = AuthService()


@router.post(
  '/get_token',
  response_model=Token,
  response_description="Returns user access token",
  summary="Authenticate API user",
  description="Authenticate an API user and return a token for subsequent requests"
)
async def get_token(body: AuthUser):
    a = await auth.login(body.username, body.password)
    if a and a["status"] == "error":
        raise HTTPException(status_code=400, detail={"status": "error", "message": a["message"]})
    return {"access_token": a["token"], "token_type": "bearer"}


@router.get(
  '/me',
  response_model=User_Pydantic,
)
async def get_token(current_user: User_Pydantic = Depends(get_current_user), token: str = Depends(APIKeyHeader(name='kekpek'))
):
    return current_user
