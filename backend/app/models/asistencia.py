from sqlalchemy import (
    Column,
    BigInteger,
    Date,
    Boolean,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.database import Base

class Asistencia(Base):
    __tablename__ = "asistencias"

    id_asistencia = Column(
        BigInteger,
        primary_key=True,
        index=True
    )

    id_carga = Column(
        BigInteger,
        ForeignKey("carga_academica.id_carga")
    )

    fecha = Column(Date)

    asistencia = Column(Boolean)

    carga = relationship("CargaAcademica")