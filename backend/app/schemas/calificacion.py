from pydantic import BaseModel
from datetime import datetime
from typing import Optional

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
