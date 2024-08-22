from sqlalchemy import Column
from config.db import Base
from sqlalchemy.sql.sqltypes import Integer,String

class ParametrosToken(Base):
    __tablename__ = "PARAMETROS_TOKEN"
    ID = Column(Integer,primary_key=True,autoincrement=True)
    SECRETE_KEY = Column(String)
    TOKEN_SECONDS_EXP = Column(Integer)
    ALGORITHM = Column(String)