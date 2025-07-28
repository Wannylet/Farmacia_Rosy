from sqlmodel import create_engine, Session

PROTOCOLO_DRIVER = "mysql+pymysql://"
USUARIO = "root"
CLAVE = "12345"
HOST = "localhost"
BASE_DATOS = "Farmacia_Rosy"
DATABASE_URL = f"{PROTOCOLO_DRIVER}{USUARIO}:{CLAVE}@{HOST}/{BASE_DATOS}"

engine = create_engine(DATABASE_URL, echo=True)


def get_sesion():
    with Session(engine) as sesion:
        yield sesion
