from sqlalchemy import Column
from config.db import Base
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, DateTime
from sqlalchemy.schema import ForeignKey
from model import TipoDocumentoModel, LicenciasModel, TipoUsuariosModel
from sqlalchemy.orm import relationship

class Usuarios(Base):
    __tablename__ = "USUARIOS"
    ID = Column(Integer,primary_key=True,autoincrement=True)
    USUARIO = Column(String(255), nullable=False)
    CONTRASEÑA = Column(String, nullable=False)
    DOCUMENTO = Column(String(20), nullable=False)
    NOMBRES = Column(String(255), nullable=False)
    APELLIDOS = Column(String(255), nullable=False)
    CORREO_ELECTRONICO = Column(String(500), nullable=False)
    TELEFONO = Column(String(50))
    ESTADO = Column(Boolean, nullable=False)
    ID_LICENCIAS = Column(Integer, ForeignKey(LicenciasModel.Licencias.ID))
    ID_TIPO_USUARIOS = Column(Integer, ForeignKey(TipoUsuariosModel.TipoUsuarios.ID))
    FECHA_CREACION = Column(DateTime)
    FECHA_MODIFICACION = Column(DateTime)
    ID_TIPO_DOCUMENTO = Column(Integer, ForeignKey(TipoDocumentoModel.TipoDocumentos.ID))

TIPO_USUARIOS = relationship("TipoUsuarios", back_populates="TIPO_USUARIOS")
LICENCIAS = relationship("Licencias", back_populates="LICENCIAS")
TIPO_DOCUMENTOS = relationship("TipoDocumentos", back_populates="TIPO_DOCUMENTOS")