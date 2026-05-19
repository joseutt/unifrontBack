from datetime import date
from typing import Optional

from pydantic import BaseModel


class AsistenciaBase(BaseModel):
    id_carga: int
    fecha: date
    asistencia: bool


class AsistenciaCreate(AsistenciaBase):
    pass


class AsistenciaUpdate(BaseModel):
    id_carga: Optional[int] = None
    fecha: Optional[date] = None
    asistencia: Optional[bool] = None


class AsistenciaResponse(AsistenciaBase):
    id_asistencia: int

    class Config:
        from_attributes = True
