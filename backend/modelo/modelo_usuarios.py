from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Usuarios(SQLModel, table=True):
    __tablename__ = "Usuarios"  # <-- nombre explícito
    id_usuarios: Optional[int] = Field(default=None, primary_key=True)
    nombre_usuario: str = Field(max_length=20)
    contrasena: str = Field(max_length=255)
    id_rol: int  # Asume que ya tienes una tabla Roles
    activo: bool
    fecha_registro: datetime
