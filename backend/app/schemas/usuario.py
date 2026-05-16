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

class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido_paterno: Optional[str] = None
    apellido_materno: Optional[str] = None
    correo: Optional[EmailStr] = None
    telefono: Optional[str] = None
    password: Optional[str] = None
    estado: Optional[str] = None

class UsuarioResponse(UsuarioBase):
    id_usuario: int
    estado: str
    fecha_creacion: datetime

    class Config:
        from_attributes = True
