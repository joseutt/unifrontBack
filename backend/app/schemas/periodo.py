from pydantic import BaseModel
from datetime import date

class PeriodoBase(BaseModel):
    nombre: str
    fecha_inicio: date
    fecha_fin: date

class PeriodoCreate(PeriodoBase):
    pass

class PeriodoResponse(PeriodoBase):
    id_periodo: int
    estado: str

    class Config:
        from_attributes = True