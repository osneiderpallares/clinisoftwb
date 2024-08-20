from pydantic import BaseModel
from typing import Optional

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
    FECHA_CREACION:str
    FECHA_MODIFICACION:str
