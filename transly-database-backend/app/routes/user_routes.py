from fastapi import APIRouter, Header, HTTPException
from app.db import get_db
from app.auth_utils import get_current_user_id
from app.models.user_model import UserResponse

router = APIRouter(prefix="/user", tags=["User"])

@router.get(
    "/me",
    response_model=UserResponse,
    openapi_extra={"security": [{"BearerAuth": []}]}
)
async def get_me(Authorization: str = Header(None)):
    if Authorization is None:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    user_id = get_current_user_id(Authorization)

    database = await get_db()
    user = await database.users.find_one({"id": user_id})

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return UserResponse(
        id=user["id"],
        username=user["username"],
        email=user["email"],
        created_at=user["created_at"]
    )
