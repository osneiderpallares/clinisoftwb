from sqlalchemy import Table, Column
from config.db import Base
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship

class TipoUsuarios(Base):
    __tablename__ = 'TIPO_USUARIOS'
    ID = Column(Integer,primary_key=True,autoincrement=True)
    NOMBRE = Column(String(255))
    ESTADO = Column(Boolean, nullable=False)

TIPO_USUARIOS = relationship("Usuarios", back_populates="TIPO_USUARIOS")