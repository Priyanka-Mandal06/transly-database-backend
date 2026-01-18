from fastapi import APIRouter, UploadFile, File, Header, HTTPException
from app.db import get_db
from app.auth_utils import get_current_user_id
from app.models.speech_model import SpeechData
import os
import uuid

router = APIRouter(prefix="/speech", tags=["Speech"])

AUDIO_DIR = "uploads/audio"
os.makedirs(AUDIO_DIR, exist_ok=True)

@router.post("/upload", openapi_extra={"security": [{"BearerAuth": []}]})
async def upload_audio(
    audio: UploadFile = File(...),
    Authorization: str = Header(None)
):
    if Authorization is None:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    user_id = get_current_user_id(Authorization)

    # Save audio locally
    file_id = str(uuid.uuid4())
    file_path = f"{AUDIO_DIR}/{file_id}_{audio.filename}"

    with open(file_path, "wb") as f:
        f.write(await audio.read())

    return {
        "message": "Audio uploaded",
        "file_path": file_path,
        "user_id": user_id
    }


@router.post("/save", openapi_extra={"security": [{"BearerAuth": []}]})
async def save_speech(data: SpeechData, Authorization: str = Header(None)):
    if Authorization is None:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    user_id = get_current_user_id(Authorization)
    data.user_id = user_id

    database = await get_db()
    result = await database.speech_history.insert_one(data.dict())

    return {"status": "saved", "id": str(result.inserted_id)}


@router.get("/history", openapi_extra={"security": [{"BearerAuth": []}]})
async def speech_history(Authorization: str = Header(None)):
    if Authorization is None:
        raise HTTPException(status_code=401, detail="Authorization header missing")

    user_id = get_current_user_id(Authorization)

    database = await get_db()
    cursor = database.speech_history.find({"user_id": user_id})
    records = await cursor.to_list(100)

    for r in records:
        r["_id"] = str(r["_id"])

    return records

