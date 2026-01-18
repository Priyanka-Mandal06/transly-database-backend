from pydantic import BaseModel
from datetime import datetime

class SpeechData(BaseModel):
    user_id: str | None = None
    extracted_text: str
    translated_text: str
    language: str
    audio_url: str | None = None
    created_at: datetime = datetime.utcnow()
