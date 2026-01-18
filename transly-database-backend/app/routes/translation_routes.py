from fastapi import APIRouter, Header, HTTPException
from app.db import get_db
from app.models.translation_model import Translation
from app.auth_utils import get_current_user_id

router = APIRouter(prefix="/translate", tags=["Translation"])

@router.post("/save", openapi_extra={"security": [{"BearerAuth": []}]})
async def save_translation(data: Translation, Authorization: str = Header(None)):
    if Authorization is None:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    user_id = get_current_user_id(Authorization)

    database = await get_db()
    data.user_id = user_id

    result = await database.translations.insert_one(data.dict())
    return {"status": "saved", "id": str(result.inserted_id)}


@router.get("/history", openapi_extra={"security": [{"BearerAuth": []}]})
async def get_history(Authorization: str = Header(None)):
    if Authorization is None:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    user_id = get_current_user_id(Authorization)

    database = await get_db()
    cursor = database.translations.find({"user_id": user_id})
    translations = await cursor.to_list(100)

    for t in translations:
        t["_id"] = str(t["_id"])

    return translations
