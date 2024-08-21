from sqlalchemy import Column
from config.db import Base
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from sqlalchemy.orm import relationship

class TipoDocumentos(Base):
    __tablename__ = "TIPO_DOCUMENTOS"
    ID = Column(Integer,primary_key=True,autoincrement=True)
    ABREVIACION = Column(String(50))
    DESCRIPCION = Column(String(255))
    ESTADO = Column(Boolean, nullable=False)

#TIPO_DOCUMENTOS = relationship("Usuarios", back_populates="TIPO_DOCUMENTOS")