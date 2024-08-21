from sqlalchemy.orm import Session 
from fastapi import HTTPException,status 
from service import UserService,GeneralService
from schema.UserSchema import UsuarioSchema

def crear_usuario(usuario:UsuarioSchema,db:Session):
    new_user = UserService.construir_usuario(usuario,db)
    GeneralService.create(new_user,db)

def obtener_usuario(user_id,db:Session):
    return UserService.obtener_usuario(user_id,db)

def obtener_usuarios(db:Session):
    return UserService.obtener_usuarios(db) # type: ignore
