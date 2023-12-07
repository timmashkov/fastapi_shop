from sqlalchemy.ext.asyncio import AsyncSession

from core.models import Chat


async def add_message(session: AsyncSession, message: str):
    chat = Chat(message=message)
    session.add(chat)
    await session.commit()
    return chat
