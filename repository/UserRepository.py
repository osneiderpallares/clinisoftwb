from sqlalchemy.orm import Session 
from model import usuario
from fastapi import HTTPException,status 
from config.db import engine
#from app.hashing import Hash

def crear_usuario(usuario,db:Session):
    usuario = usuario.dict()    
    try:
        nuevo_usuario = usuario.Usuarios(
            USUARIO=usuario["USUARIO"],
            CONTRASEÑA=usuario["CONTRASEÑA"],
            DOCUMENTO=usuario["DOCUMENTO"],
            NOMBRES=usuario["NOMBRES"],
            APELLIDOS=usuario["APELLIDOS"],
            CORREO_ELECTRONICO=usuario["CORREO_ELECTRONICO"],
            TELEFONO=usuario["TELEFONO"],
            ESTADO=usuario["ESTADO"],
            ID_LICENCIAS=usuario["ID_LICENCIAS"],
            ID_TIPO_USUARIOS=usuario["ID_TIPO_USUARIOS"],
            FECHA_CREACION=usuario["FECHA_CREACION"],
            FECHA_MODIFICACION=usuario["FECHA_MODIFICACION"]
        )
        db.add(nuevo_usuario)
        db.commit()
        db.refresh(nuevo_usuario)
    except Exception as e :
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Error creando usuario {e}"
        )
