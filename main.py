import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

# Montar el directorio static para servir archivos estáticos como CSS, imágenes, etc.
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar Jinja2 para renderizar plantillas HTML
templates = Jinja2Templates(directory="templates")

# Ruta para la página principal (Índice)
@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

# Ruta para la página principal (Índice)
@app.get("/Grafica", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("Grafica1.html", {"request": request})

@app.get("/Grafica2", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("Grafica2.html", {"request": request})

@app.get("/Grafica3", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("Grafica3.html", {"request": request})

@app.get("/Grafica4", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("Grafica4.html", {"request": request})

@app.get("/objetivo", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("objetivo.html", {"request": request})