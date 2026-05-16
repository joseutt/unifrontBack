from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UsuarioBase(BaseModel):
    nombre: str
    apellido_paterno: str
    apellido_materno: Optional[str] = None
    correo: EmailStr
    telefono: Optional[str] = None

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioResponse(UsuarioBase):
    id_usuario: int
    estado: str
    fecha_creacion: datetime

    class Config:
        from_attributes = True