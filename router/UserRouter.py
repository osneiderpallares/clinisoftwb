from fastapi import APIRouter, Depends, status 
from fastapi import FastAPI, Request, Form, HTTPException, Cookie  
from typing import Annotated
from fastapi.responses import HTMLResponse, RedirectResponse
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi.templating import Jinja2Templates
from schema.UserSchema import UsuarioSchema
from repository import UserRepository
from sqlalchemy.orm import Session 
from config.db import get_db

RouterUser = APIRouter()
Jinja2_Templates = Jinja2Templates(directory="templates")

SECRETE_KEY = "73bb6bcb1e1693673a7ed25d9607bc287dd9298505bd455686bb94ded8ba0fe6"
TOKEN_SECONDS_EXP = 60
ALGORITHM = "HS256"

db_usuarios = {
    "osneider":{
        "id":0,
        "usuario":"osneider",
        "contraseña":"123"
    }
}

def get_usuario(usuario:str,db:list):

    if usuario in db:
        return db[usuario] # type: ignore
    
def autenticacion_usuario(contraseña:str, contraseña_plano:str):
    if contraseña_plano == contraseña:
        return True
    return False

def crear_token(data:list):
    data_token = data.copy()
    data_token["exp"] = datetime.utcnow() + timedelta(seconds=TOKEN_SECONDS_EXP)  # type: ignore
    token_jwt = jwt.encode(data_token, key=SECRETE_KEY, algorithm="HS256") # type: ignore
    return token_jwt

@RouterUser.get("/dashboard", response_class=HTMLResponse)
def dashboard(request:Request, access_token:Annotated[str | None, Cookie()]= None):
    if access_token is None:
        return RedirectResponse("/", status_code=302)
    try:
        datos_usuario = jwt.decode(access_token,key=SECRETE_KEY,algorithms=ALGORITHM)
        if get_usuario(datos_usuario["usuario"],db_usuarios) is None: # type: ignore
            return RedirectResponse("/", status_code=302)
        return Jinja2_Templates.TemplateResponse("dashboard.html",{"request": request})
    except JWTError:
        return RedirectResponse("/", status_code=302)    

@RouterUser.post("/login")
def login(usuario:Annotated[str, Form()],contraseña: Annotated[str, Form()]):
    datos = get_usuario(usuario, db_usuarios) # type: ignore
    if datos is None:
        raise HTTPException(
            status_code=401,
            detail="Usuario no autorizado"
        )
    if not autenticacion_usuario(datos["contraseña"], contraseña):
        raise HTTPException(
            status_code=401,
            detail="Usuario no autorizado"
        )
    token = crear_token({"usuario":datos["usuario"]}) # type: ignore
    return RedirectResponse(
        "/dashboard", 
        status_code=302,
        headers={"set-cookie":f"access_token={token}; Max-Age={TOKEN_SECONDS_EXP}"} 
        )
    
@RouterUser.post("/logout")
def logout():
    return RedirectResponse("/", status_code=302, headers={
        "set-cookie": "access_token=; Max-Age=0"
    })

@RouterUser.post('/register',status_code=status.HTTP_201_CREATED)
def crear_usuario(usuario:UsuarioSchema,db:Session = Depends(get_db)):    
    UserRepository.crear_usuario(usuario,db)
    return {"respuesta":"Usuario creado satisfactoriamente!!"}

# @RouterUser.get('/{user_id}',status_code=status.HTTP_200_OK)
# def obtener_usuario(user_id:int,db:Session = Depends(get_db)):
#     usuario = UserRepository.obtener_usuario(user_id,db)
#     return usuario

@RouterUser.get('/get')
def obtener_usuarios(db:Session = Depends(get_db)):
    return UserRepository.obtener_usuarios(db)