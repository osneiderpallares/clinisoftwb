from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UsuarioSchema(BaseModel):
    ID:Optional[int]
    USUARIO: str
    CONTRASEÑA: str    
    DOCUMENTO: str
    NOMBRES:str
    APELLIDOS:str
    CORREO_ELECTRONICO:str
    TELEFONO:str
    ESTADO:bool
    ID_LICENCIAS:int
    ID_TIPO_USUARIOS:int
    FECHA_CREACION: Optional[str]
    FECHA_MODIFICACION: Optional[str]
    ID_TIPO_DOCUMENTO:int