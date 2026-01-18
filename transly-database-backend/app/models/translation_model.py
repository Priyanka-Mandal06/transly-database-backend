from pydantic import BaseModel
from typing import Optional

class Translation(BaseModel):
    inputText: str
    translatedText: str
    sourceLanguage: str
    targetLanguage: str
    user_id: Optional[str] = None  
