from pydantic import BaseModel
from typing import Optional

class CarreraBase(BaseModel):
    clave: str
    nombre: str
    nivel: str
    duracion_cuatrimestres: int

class CarreraCreate(CarreraBase):
    pass

class CarreraUpdate(BaseModel):
    clave: Optional[str] = None
    nombre: Optional[str] = None
    nivel: Optional[str] = None
    duracion_cuatrimestres: Optional[int] = None
    estado: Optional[bool] = None

class CarreraResponse(CarreraBase):
    id_carrera: int
    estado: bool

    class Config:
        from_attributes = True
