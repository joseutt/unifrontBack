from fastapi import FastAPI

from app.models import init as _models_init
from app.routers import (
    usuarios,
    carreras,
    alumnos,
    docentes,
    materias,
    periodos,
    parciales,
    calificaciones,
    titulaciones,
    roles,
    auth,
    documentos
)

app = FastAPI(
    title="Unifront API", version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "API funcionando"}

# ROUTERS

app.include_router(usuarios.router)
app.include_router(carreras.router)
app.include_router(alumnos.router)
app.include_router(docentes.router)
app.include_router(materias.router)
app.include_router(periodos.router)
app.include_router(parciales.router)
app.include_router(calificaciones.router)
app.include_router(titulaciones.router)
# app.include_router(roles.router)
app.include_router(auth.router)
app.include_router(documentos.router)
