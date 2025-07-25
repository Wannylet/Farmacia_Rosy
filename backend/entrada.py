# FastAPI
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

# Rutas
from backend.router.iniciar_sesion import router as router_iniciar_sesion

# Librerias
import os

app = FastAPI()

# Ruta absoluta a la carpeta frontend
frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend")

# Servir archivos estáticos desde la carpeta frontend
app.mount("/frontend", StaticFiles(directory=frontend_path, html=True), name="frontend")

# (Opcional) Ruta explícita para /
@app.get("/")
async def srv_iniciar_sesion():
	return FileResponse("frontend/iniciar-sesion.html")

app.include_router(router_iniciar_sesion)