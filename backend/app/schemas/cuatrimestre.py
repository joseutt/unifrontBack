from pydantic import BaseModel


class CuatrimestreSimple(BaseModel):
    id_cuatrimestre: int
    nombre: str

    class Config:
        from_attributes = True