from sqlalchemy import Table, Column
from config.db import Base
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, DateTime
from config.db import engine, meta_data
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship

class Usuarios(Base):
    __tablename__ = "USUARIOS"
    ID = Column(Integer,primary_key=True,autoincrement=True)
    USUARIO = Column(String(255), nullable=False)
    CONTRASEÑA = Column(String(500), nullable=False)
    ID_TIPO_DOCUMENTO = Column(Integer)
    DOCUMENTO = Column(String(20), nullable=False)
    NOMBRES = Column(String(255), nullable=False)
    APELLIDOS = Column(String(255), nullable=False)
    CORREO_ELECTRONICO = Column(String(500), nullable=False)
    TELEFONO = Column(String(255))
    ESTADO = Column(Boolean,nullable=False)
    ID_LICENCIA = Column(Integer)
    ID_TIPO_USUARIO = Column(Integer)
    FECHA_CREACION = Column(DateTime)
    FECHA_MODIFICACION = Column(DateTime)
