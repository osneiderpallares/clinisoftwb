from sqlalchemy import Table, Column
from config.db import Base
from sqlalchemy.sql.sqltypes import Integer, String, Boolean, DateTime
from sqlalchemy.orm import relationship

class Licencias(Base):
    __tablename__ = 'LICENCIAS'
    ID = Column(Integer,primary_key=True,autoincrement=True)
    DESCRIPCION = Column(String(255))
    ESTADO = Column(Boolean, nullable=False)

LICENCIAS = relationship("Licencias", back_populates="LICENCIA")