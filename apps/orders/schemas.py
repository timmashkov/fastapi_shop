from pydantic import BaseModel


class OrderIn(BaseModel):
    promocode: str | None = None


class OrderOut(OrderIn):
    id: int
