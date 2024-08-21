from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class TipoDocumentoSchema(BaseModel):
    ID:Optional[int]    
    ABREVIACION:str    
    DESCRIPCION:str    
    ESTADO:bool    