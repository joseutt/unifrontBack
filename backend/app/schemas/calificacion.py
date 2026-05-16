from pydantic import BaseModel
from datetime import datetime

class CalificacionBase(BaseModel):
    id_carga: int
    id_parcial: int
    calificacion: float
    capturado_por: int

class CalificacionCreate(CalificacionBase):
    pass

class CalificacionResponse(CalificacionBase):
    id_calificacion: int
    fecha_captura: datetime

    class Config:
        from_attributes = True