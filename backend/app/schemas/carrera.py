from pydantic import BaseModel

class CarreraBase(BaseModel):
    clave: str
    nombre: str
    nivel: str
    duracion_cuatrimestres: int

class CarreraCreate(CarreraBase):
    pass

class CarreraResponse(CarreraBase):
    id_carrera: int
    estado: bool

    class Config:
        from_attributes = True