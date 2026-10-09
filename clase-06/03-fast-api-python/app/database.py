from sqlmodel import SQLModel, Session, create_engine

DATABASE_URL = "sqlite:///./productos.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


def crear_tablas():
    SQLModel.metadata.create_all(engine)


def obtener_sesion():
    with Session(engine) as sesion:
        yield sesion
