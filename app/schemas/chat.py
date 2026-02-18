from datetime import datetime

from pydantic import BaseModel


class MessageCreate(BaseModel):
    content: str
    type: str = "text"
    reply_to: int | None = None


class MessageOut(BaseModel):
    id: int
    chat_id: int
    sender_id: int
    content: str
    type: str
    created_at: datetime

    class Config:
        from_attributes = True
