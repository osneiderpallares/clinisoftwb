from sqlalchemy.orm import Session
from service import UserService,GeneralService
from schema.UserSchema import UsuarioSchema

def crear_usuario(usuario:UsuarioSchema,db:Session):
    new_user = UserService.construir_usuario(usuario,db)
    GeneralService.create(new_user,db)

def obtener_usuario(user_id,db:Session):
    return UserService.obtener_usuario(user_id,db)

def obtener_usuarios(db:Session):
    return UserService.obtener_usuarios(db)

def validar_usuario(usuario:str,contraseña:str,db:Session):  
    result = UserService.validar_usuario(usuario, contraseña, db)    
    return result

def crear_token(data:list,db:Session):
    parametros = GeneralService.object_as_dict(GeneralService.token_parameters(db))    
    return GeneralService.crear_token(data,parametros)

def decode_token(access_token,db:Session):
    parametros = GeneralService.object_as_dict(GeneralService.token_parameters(db))
    return GeneralService.decode_token(access_token,parametros)
    
def get_seconds_exp(db:Session):
    return GeneralService.object_as_dict(GeneralService.token_parameters(db))