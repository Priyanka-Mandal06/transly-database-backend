from pydantic import BaseModel
from datetime import datetime

class OCRData(BaseModel):
    user_id: str | None = None
    extracted_text: str
    detected_language: str
    translated_text: str
    image_url: str | None = None
    created_at: datetime = datetime.utcnow()
