# backend/servicios/auth.py

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from pydantic import BaseModel
from datetime import datetime, timedelta
from backend.modelos.modelo_usuarios import Usuarios

SECRET_KEY = "_FGGhjZJjWTtYp1nX2Tqe7hTNgtBVGQ7722Fn7dPbiF_bveqTW_W_uCZK6zIY4EiQWrTn_dDm89msI_q65Sh6w"
ALGORITHM = "HS256"
EXPIRACION_MINUTOS = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/autenticar-usuario")

def crear_token(usuario: Usuarios):
    expiracion = datetime.utcnow() + timedelta(minutes=EXPIRACION_MINUTOS)
    datos = {"sub": usuario.nombre_usuario, "exp": expiracion}
    token = jwt.encode(datos, SECRET_KEY, algorithm=ALGORITHM)
    return token

class TokenData(BaseModel):
    username: str | None = None

def verificar_token(token: str = Depends(oauth2_scheme)) -> TokenData:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str | None = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        return TokenData(username=username)
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Token inválido o expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )