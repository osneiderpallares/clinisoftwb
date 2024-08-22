from fastapi import APIRouter, Depends, status 
from fastapi import Request, Form, HTTPException, Cookie  
from typing import Annotated
from fastapi.responses import HTMLResponse, RedirectResponse
from jose import JWTError
from fastapi.templating import Jinja2Templates
from schema.UserSchema import UsuarioSchema
from repository import UserRepository
from sqlalchemy.orm import Session 
from config.db import get_db

RouterUser = APIRouter()
Jinja2_Templates = Jinja2Templates(directory="templates")

@RouterUser.get("/dashboard", response_class=HTMLResponse,tags=["Dashboard"])
def dashboard(request:Request, access_token:Annotated[str | None, Cookie()]= None, db:Session = Depends(get_db)):
    if access_token is None:
        return RedirectResponse("/", status_code=302)
    try:
        datos_usuario = UserRepository.decode_token(access_token,db)
        if UserRepository.validar_usuario(datos_usuario["usuario"],datos_usuario["contraseña"],db) is None:
            return RedirectResponse("/", status_code=302)
        return Jinja2_Templates.TemplateResponse("dashboard.html",{"request": request})      
    except JWTError:
        return RedirectResponse("/", status_code=302)    

@RouterUser.post("/login", tags=["User"])
def login(usuario:Annotated[str, Form()],contraseña: Annotated[str, Form()],db:Session = Depends(get_db)):    
    user = UserRepository.validar_usuario(usuario,contraseña,db)    
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Usuario y/o contraseña incorrectos"
        )
    token = UserRepository.crear_token({"usuario":user["USUARIO"],"contraseña":contraseña},db) # type: ignore 
    TOKEN_SECONDS_EXP = UserRepository.get_seconds_exp(db)
    return RedirectResponse("/dashboard", 
        status_code=302,
        headers={"set-cookie":f"access_token={token}; Max-Age={TOKEN_SECONDS_EXP}"}         
        )
    
@RouterUser.post("/logout",tags=["User"])
def logout():
    return RedirectResponse("/", status_code=302, headers={
        "set-cookie": "access_token=; Max-Age=0"
    })

@RouterUser.post('/register',status_code=status.HTTP_201_CREATED,tags=["User"])
def crear_usuario(usuario:UsuarioSchema,db:Session = Depends(get_db)):    
    UserRepository.crear_usuario(usuario,db)
    return {"respuesta":"Usuario creado satisfactoriamente!!"}

@RouterUser.get('/get',tags=["User"])
def obtener_usuarios(db:Session = Depends(get_db)):
    return UserRepository.obtener_usuarios(db)