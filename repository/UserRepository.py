from sqlalchemy.orm import Session
from service import UserService,GeneralService
from schema.UserSchema import UsuarioSchema
from model import UserModel

def crear_usuario(usuario,db:Session):
    GeneralService.create(usuario,db)    

def obtener_usuario(user_id,db:Session):
    return db.query(UserModel.Usuarios).filter(UserModel.Usuarios.ID == user_id).first()

def obtener_usuarios(db:Session):
    return db.query(UserModel.Usuarios).filter(UserModel.Usuarios.ESTADO == True).all()

def get_usuario(usuario:str,db:Session):
    return db.query(UserModel.Usuarios).filter(UserModel.Usuarios.USUARIO == usuario).first()