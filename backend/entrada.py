# FastAPI
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

# Rutas
from backend.routers.iniciar_sesion import router as router_iniciar_sesion

# Librerias
import os

app = FastAPI()

# Ruta absoluta a la carpeta frontend
ruta_dist = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "frontend", "dist"))

# Servir archivos estáticos desde la carpeta frontend
app.mount("/", StaticFiles(directory=ruta_dist, html=True), name="frontend")

# Ruta fallback para Vue Router (todas las rutas no encontradas van a index.html)
@app.get("/{full_path:path}")
async def retroceso_vue_router(full_path: str):
    return FileResponse(os.path.join(ruta_dist, "index.html"))

app.include_router(router_iniciar_sesion)