from pydantic import BaseModel
from typing import Optional
from datetime import date

class AlumnoBase(BaseModel):
    matricula: str
    numero_control: Optional[str] = None

    id_usuario: int
    id_carrera: int
    id_plan: int

    fecha_nacimiento: Optional[date] = None

    ciudad_nacimiento: Optional[str] = None
    municipio_nacimiento: Optional[str] = None

    nacionalidad: Optional[str] = None

    sexo: Optional[str] = None

    curp: Optional[str] = None

    direccion: Optional[str] = None

    ciudad: Optional[str] = None
    estado: Optional[str] = None

    correo_contacto: Optional[str] = None

    fecha_ingreso: Optional[date] = None

    foto: Optional[str] = None

class AlumnoCreate(AlumnoBase):
    pass

class AlumnoResponse(AlumnoBase):
    id_alumno: int
    estatus: str

    class Config:
        from_attributes = True

class AlumnoUpdate(BaseModel):
    matricula: Optional[str] = None
    numero_control: Optional[str] = None
    id_usuario: Optional[int] = None
    id_carrera: Optional[int] = None
    id_plan: Optional[int] = None
    fecha_nacimiento: Optional[date] = None
    ciudad_nacimiento: Optional[str] = None
    municipio_nacimiento: Optional[str] = None
    nacionalidad: Optional[str] = None
    sexo: Optional[str] = None
    curp: Optional[str] = None
    direccion: Optional[str] = None
    ciudad: Optional[str] = None
    estado: Optional[str] = None
    correo_contacto: Optional[str] = None
    fecha_ingreso: Optional[date] = None
    estatus: Optional[str] = None
    foto: Optional[str] = None

    class Config:
        from_attributes = True
