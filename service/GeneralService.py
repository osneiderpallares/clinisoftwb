from sqlalchemy.orm import Session 
from fastapi import HTTPException,status

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