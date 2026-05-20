from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

from app.schemas.detalles import (
    AlumnoDetalle,
    GrupoMateriaDetalleResponse,
    ParcialDetalle
)

class CalificacionBase(BaseModel):
    id_carga: int
    id_parcial: int
    calificacion: float
    capturado_por: int

class CalificacionCreate(CalificacionBase):
    pass

class CalificacionUpdate(BaseModel):
    id_carga: Optional[int] = None
    id_parcial: Optional[int] = None
    calificacion: Optional[float] = None
    capturado_por: Optional[int] = None

class CalificacionResponse(CalificacionBase):
    id_calificacion: int
    fecha_captura: datetime

    class Config:
        from_attributes = True


class CapturaCalificacionItem(BaseModel):
    id_carga: int
    id_parcial: int
    calificacion: Optional[float] = Field(default=None, ge=0, le=100)


class CapturaCalificacionesBatch(BaseModel):
    grupo_materia_id: int
    calificaciones: list[CapturaCalificacionItem]


class CapturaAlumnoCalificacionResponse(BaseModel):
    id_calificacion: Optional[int] = None
    id_carga: int
    id_parcial: int
    calificacion: Optional[float] = None


class CapturaAlumnoResponse(BaseModel):
    id_carga: int
    estatus: Optional[str] = None
    alumno: Optional[AlumnoDetalle] = None
    calificaciones: list[CapturaAlumnoCalificacionResponse] = Field(
        default_factory=list
    )


class CapturaCalificacionesResponse(BaseModel):
    grupo_materia: GrupoMateriaDetalleResponse
    parciales: list[ParcialDetalle]
    alumnos: list[CapturaAlumnoResponse]
