from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.entities import Chat, Message
from app.schemas.chat import MessageCreate


async def list_chats(db: AsyncSession, limit: int = 50) -> list[Chat]:
    result = await db.scalars(select(Chat).order_by(desc(Chat.created_at)).limit(limit))
    return list(result)


async def list_messages(db: AsyncSession, chat_id: int, limit: int = 100) -> list[Message]:
    result = await db.scalars(
        select(Message).where(Message.chat_id == chat_id).order_by(desc(Message.created_at)).limit(limit)
    )
    return list(reversed(list(result)))


async def send_message(db: AsyncSession, chat_id: int, sender_id: int, payload: MessageCreate) -> Message:
    message = Message(
        chat_id=chat_id,
        sender_id=sender_id,
        content=payload.content,
        type=payload.type,
        reply_to=payload.reply_to,
    )
    db.add(message)
    await db.commit()
    await db.refresh(message)
    return message
