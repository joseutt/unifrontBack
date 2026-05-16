from pydantic import BaseModel

class RolBase(BaseModel):
    nombre: str

class RolCreate(RolBase):
    pass

class RolResponse(RolBase):
    id_rol: int

    class Config:
        from_attributes = True