from pydantic import BaseModel

class ParcialBase(BaseModel):
    nombre: str
    porcentaje: float

class ParcialCreate(ParcialBase):
    pass

class ParcialResponse(ParcialBase):
    id_parcial: int

    class Config:
        from_attributes = True