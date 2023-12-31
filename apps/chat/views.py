from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import vortex
from core.models import Chat

router = APIRouter(prefix="/chat")

"""
Using websockets for interactive chat
creating a class ConnectionManager with custom methods
"""


class ConnectionManager:
    def __init__(self) -> None:
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket) -> None:
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket) -> None:
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket) -> None:
        await websocket.send_text(message)

    async def broadcast(self, message: str, add_to_db: bool) -> None:
        if add_to_db:
            await self.add_messages_to_db(message=message)
        for connection in self.active_connections:
            await connection.send_text(message)

    @staticmethod
    async def add_messages_to_db(message: str) -> None:
        session = vortex.session_factory()
        async with session as sess:
            stmt = Chat(message=message)
            sess.add(stmt)
            await sess.commit()


manager = ConnectionManager()


@router.get("/last_messages")
async def get_last_messages(
    session: AsyncSession = Depends(vortex.scoped_session_dependency),
) -> list:
    """
    Getting last 5 messages endpoint
    :param session:
    :return:
    """
    query = select(Chat).order_by(Chat.id.desc()).limit(5)
    result = await session.execute(query)
    answer = result.all()
    var_list = [msg[0].as_dict() for msg in answer]
    return var_list


@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int) -> None:
    """
    Async func for making chat
    :param websocket:
    :param client_id:
    :return:
    """
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Client #{client_id} says: {data}", add_to_db=True)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat", add_to_db=False)
