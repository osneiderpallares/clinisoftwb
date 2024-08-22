from sqlalchemy.orm import Session 
from model import UserModel
from fastapi import HTTPException,status 
import bcrypt
from schema.UserSchema import UsuarioSchema
from passlib.context import CryptContext
from service import GeneralService

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def construir_usuario(usuario:UsuarioSchema,db:Session):   
    # password = usuario.CONTRASEÑA
    # salt = bcrypt.gensalt()
    # hashed_password = bcrypt.hashpw(password.encode("utf-8"), salt)      
    # usuario.CONTRASEÑA = hashed_password.decode("utf-8")     
    try:       
        nuevo_usuario = UserModel.Usuarios(            
            USUARIO = usuario.USUARIO,
            CONTRASEÑA = get_password_hash(usuario.CONTRASEÑA),
            ID_TIPO_DOCUMENTO = usuario.ID_TIPO_DOCUMENTO,
            DOCUMENTO = usuario.DOCUMENTO,
            NOMBRES = usuario.NOMBRES,
            APELLIDOS = usuario.APELLIDOS,
            CORREO_ELECTRONICO = usuario.CORREO_ELECTRONICO,
            TELEFONO = usuario.TELEFONO,
            ESTADO = usuario.ESTADO,
            ID_LICENCIAS = usuario.ID_LICENCIAS,
            ID_TIPO_USUARIOS = usuario.ID_TIPO_USUARIOS,
            FECHA_CREACION = usuario.FECHA_CREACION,
            FECHA_MODIFICACION = usuario.FECHA_MODIFICACION,
        )
       
        #return UsuarioSchema(**usuario) # type: ignore
        return nuevo_usuario
      
    except Exception as e :
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Error creando usuario {e}"
        )
    
def obtener_usuario(user_id,db:Session):
    usuario = db.query(UserModel.Usuarios).filter(UserModel.Usuarios.ID == user_id).first()    
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No existe el usuario con el id {user_id}"
        )
    
    return usuario

def obtener_usuarios(db:Session):
    usuarios = db.query(UserModel.Usuarios).filter(UserModel.Usuarios.ESTADO == True).all()    
    if not usuarios:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No existe información"
        )
    
    return usuarios

def verify_password(contraseña:str,hash:str):
    return pwd_context.verify(contraseña,hash)


def get_password_hash(contraseña:str):
    return pwd_context.hash(contraseña)


def validar_usuario(usuario:str,contraseña:str,db:Session): 
    try:
        user = GeneralService.object_as_dict(db.query(UserModel.Usuarios).filter(UserModel.Usuarios.USUARIO == usuario).first())    
        if not user:
            return None
        if not verify_password(contraseña,user["CONTRASEÑA"]):
            return None
        return user
    except Exception as e :
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Error: {e}"
        )   
    