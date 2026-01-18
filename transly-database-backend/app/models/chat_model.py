from pydantic import BaseModel
from datetime import datetime

class ChatMessage(BaseModel):
    user_id: str | None = None
    user_message: str
    bot_response: str
    created_at: datetime = datetime.utcnow()
