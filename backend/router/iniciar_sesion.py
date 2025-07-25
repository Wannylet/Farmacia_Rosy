# Router
from fastapi import APIRouter, Depends, HTTPException

# Validacion
from sqlmodel import Session, select
from pydantic import BaseModel, field_validator
import re

# Modelo
from backend.modelo.base_datos import get_sesion
from backend.modelo.modelo_usuarios import Usuarios

from backend.servicio.autenticar import crear_token

from argon2 import PasswordHasher

router = APIRouter()

# Validacion de inicio de sesion
class val_iniciar_sesion(BaseModel):
  nombre_usuario: str
  contrasena: str

  @field_validator("nombre_usuario", mode="before")
  @classmethod
  def validar_nombre_usuario(cls, nombre):
    if len(nombre) == 0:
      raise HTTPException(status_code=404, detail="El nombre de usuario no debe estar vacío")
    if len(nombre) > 20:
      raise HTTPException(status_code=404, detail="El nombre de usuario debe tener menos de 20 caracteres")
    if re.search(r"[^a-zA-Z0-9]", nombre):
      raise HTTPException(status_code=404, detail="El nombre de usuario no debe contener símbolos especiales")
    return nombre

  @field_validator("contrasena", mode="before")
  @classmethod
  def validar_contrasena(cls, contra):
    if len(contra) == 0:
      raise HTTPException(status_code=404, detail="La contraseña no debe estar vacía")
    if len(contra) < 8:
      raise HTTPException(status_code=404, detail="La contraseña debe tener al menos 8 caracteres")
    if len(contra) > 255:
      raise HTTPException(status_code=404, detail="La contraseña debe tener menos de 255 caracteres")
    if not re.search(r"[A-Z]", contra):
      raise HTTPException(status_code=404, detail="La contraseña debe contener al menos una letra mayúscula")
    if not re.search(r"[a-z]", contra):
      raise HTTPException(status_code=404, detail="La contraseña debe contener al menos una letra minúscula")
    if not re.search(r"[0-9]", contra):
      raise HTTPException(status_code=404, detail="La contraseña debe contener al menos un número")
    if re.search(r"[^a-zA-Z0-9]", contra):
      raise HTTPException(status_code=404, detail="La contraseña no debe contener símbolos especiales")
    return contra
    
@router.post("/autenticar-usuario")
async def srv_autenticar_usuario(datos: val_iniciar_sesion, sesion: Session = Depends(get_sesion)):
# Buscar usuario en la base de datos
  consulta = select(Usuarios).where(Usuarios.nombre_usuario == datos.nombre_usuario)
  resultado = sesion.exec(consulta).first()

  # Verificar contraseña
  argonPH = PasswordHasher()
  if not resultado:
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
  try:
    print(resultado.contrasena + " " + datos.nombre_usuario + " " + datos.contrasena)
    argonPH.verify(resultado.contrasena, datos.contrasena)
  except:
    raise HTTPException(status_code=401, detail="Contraseña incorrecta")
  token = crear_token(resultado)
  return {"access_token": token, "token_type": "bearer"}
