from fastapi import APIRouter, Depends
from backend.servicio.autenticar import verificar_token, TokenData

router = APIRouter()

@router.get("/principal")
def ruta_protegida(usuario: TokenData = Depends(verificar_token)):
    return {"mensaje": f"Bienvenido, {usuario.username}"}
