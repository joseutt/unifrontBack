from sqlalchemy import (
    Column,
    Integer,
    String
)

from sqlalchemy.orm import relationship

from app.database import Base

class Rol(Base):
    __tablename__ = "roles"

    id_rol = Column(Integer, primary_key=True, index=True)

    nombre = Column(
        String(50),
        unique=True,
        nullable=False
    )

    usuarios = relationship(
        "Usuario",
        secondary="usuario_roles",
        back_populates="roles"
    )