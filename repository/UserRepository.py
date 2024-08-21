from sqlalchemy.orm import Session 
from fastapi import HTTPException,status 
from service import UserService

def crear_usuario(usuario,db:Session):    
    try:
        new_user = UserService.construir_usuario(usuario,db)           
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
    except Exception as e :
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Error creando usuario {e}"
        )

def obtener_usuario(user_id,db:Session):
    return UserService.obtener_usuario(user_id,db)

def obtener_usuarios(db:Session):
    return UserService.obtener_usuarios(db)
