from fastapi import APIRouter, Header, HTTPException
from app.db import get_db
from app.auth_utils import get_current_user_id
from app.models.chat_model import ChatMessage

router = APIRouter(prefix="/chatbot", tags=["Chatbot"])

# Save chat message
@router.post("/save")
async def save_chat(data: ChatMessage, Authorization: str = Header(None)):
    if Authorization is None:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    user_id = get_current_user_id(Authorization)
    data.user_id = user_id

    database = await get_db()
    result = await database.chat_history.insert_one(data.dict())

    return {"status": "saved", "id": str(result.inserted_id)}


# Fetch chat history
@router.get("/history")
async def get_chat_history(Authorization: str = Header(None)):
    if Authorization is None:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    user_id = get_current_user_id(Authorization)

    database = await get_db()
    cursor = database.chat_history.find({"user_id": user_id})
    records = await cursor.to_list(100)

    for r in records:
        r["_id"] = str(r["_id"])

    return records
