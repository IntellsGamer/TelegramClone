from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db
from app.schemas.chat import MessageCreate, MessageOut
from app.services.chat import list_chats, list_messages, send_message

router = APIRouter(prefix="/api/chats", tags=["chats"])


@router.get("")
async def get_chats(db: AsyncSession = Depends(get_db)):
    chats = await list_chats(db)
    return [{"id": chat.id, "title": chat.title, "type": chat.type} for chat in chats]


@router.get("/{chat_id}/messages", response_model=list[MessageOut])
async def get_messages(chat_id: int, db: AsyncSession = Depends(get_db)):
    return await list_messages(db, chat_id)


@router.post("/{chat_id}/messages", response_model=MessageOut)
async def post_message(chat_id: int, payload: MessageCreate, db: AsyncSession = Depends(get_db)):
    return await send_message(db, chat_id, sender_id=1, payload=payload)
