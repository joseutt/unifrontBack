from pydantic import BaseModel

class MateriaBase(BaseModel):
    clave: str
    nombre: str
    creditos: float

class MateriaCreate(MateriaBase):
    pass

class MateriaResponse(MateriaBase):
    id_materia: int
    estado: bool

    class Config:
        from_attributes = True