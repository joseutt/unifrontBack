from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

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
    documentos,
    plan_estudio
)

app = FastAPI(
    title="Unifront API",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
app.include_router(plan_estudio.router)