from pydantic import BaseModel, ConfigDict


class ProductBase(BaseModel):
    """
    Базовая модель схемы
    """

    name: str
    description: str
    price: int


class ProductCreate(ProductBase):
    """
    Схема для создания записи
    """

    pass


class ProductUpdate(ProductCreate):
    """
    Схема для апдейта записи
    """

    pass


class ProductUpdatePartial(ProductCreate):
    """
    Схема для частичного апдейта записи
    """

    name: str | None = None
    description: str | None = None
    price: int | None = None


class Product(ProductBase):
    """
    Схема для возврата записи
    """

    model_config = ConfigDict(from_attributes=True)
    id: int
