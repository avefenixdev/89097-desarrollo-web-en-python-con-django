from sqlmodel import SQLModel, Field


class ProductoBase(SQLModel):
    nombre: str = Field(min_length=2, max_length=100)
    precio: float = Field(gt=0)
    stock: int = Field(ge=0)


class Producto(ProductoBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class ProductoCrear(ProductoBase):
    pass


class ProductoActualizar(ProductoBase):
    pass


class ProductoLeer(ProductoBase):
    id: int
