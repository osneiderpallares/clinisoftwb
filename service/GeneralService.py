from sqlalchemy.orm import Session 
from fastapi import HTTPException,status
from sqlalchemy.inspection import inspect
from model.ParametrosToken import ParametrosToken
from datetime import datetime, timedelta
from jose import jwt

def create(object,db:Session):
    try:
        db.add(object)
        db.commit()
        db.refresh(object)        
    except Exception as e :
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Error creando usuario {e}"
        )    
    
def object_as_dict(obj):
    return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}

def token_parameters(db:Session):
    try:
        result = db.query(ParametrosToken).first()
    except Exception as e :
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Error: {e}"
        )   
    return result

def crear_token(data:list,parametros):
    data_token = data.copy()
    data_token["exp"] = datetime.utcnow() + timedelta(seconds=parametros["TOKEN_SECONDS_EXP"])  # type: ignore
    return encode_token(data_token,parametros)

def encode_token(data_token,parametros):
    return jwt.encode(data_token, key=parametros["SECRETE_KEY"], algorithm=parametros["ALGORITHM"])

def decode_token(access_token,parametros):
    return jwt.decode(access_token,key=parametros["SECRETE_KEY"],algorithms=parametros["ALGORITHM"])

