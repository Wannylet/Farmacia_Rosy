from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()
# Servir archivos estáticos desde la carpeta frontend
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

# (Opcional) Ruta explícita para /
@app.get("/")
async def serve_index():
	return FileResponse("frontend/index.html")