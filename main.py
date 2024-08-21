from fastapi import FastAPI, Request, Form, HTTPException, Cookie  
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Annotated
from datetime import datetime, timedelta
from jose import jwt, JWTError
from router.UserRouter import RouterUser

app = FastAPI()
Jinja2_Templates = Jinja2Templates(directory="templates")

app.title = "CliniSoft"
app.version="0.0.1"
app.include_router(RouterUser)

@app.get("/", response_class=HTMLResponse)
def root(request:Request):
    return Jinja2_Templates.TemplateResponse("index.html",{"request": request})