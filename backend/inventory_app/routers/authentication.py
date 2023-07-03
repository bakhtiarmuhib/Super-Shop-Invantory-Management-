from fastapi import APIRouter,Depends,HTTPException, Request,status
from ..import schemas , models
from fastapi.security import OAuth2PasswordRequestForm
from ..hashing import Hash
from sqlalchemy.orm import Session
from ..database import SessionLocal
from . import JWTtoken
from pydantic import BaseModel

import json


router = APIRouter(tags=['Authentication'])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
class Token(BaseModel):
    access_token: str
    token_type: str

@router.post('/login',response_class= Token)
def login(request:OAuth2PasswordRequestForm=Depends(), db: Session = Depends(get_db)):
    
    
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail="User not found.")
    if not Hash.verify_password(request.password,user.password):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail="Incorrect password.")

    access_token = JWTtoken.create_access_token(data={'sub':user.email})
    return {'access_token': access_token,'token_type':'bearer'}


# @router.post('/sarower',)
# async def sarower(request: Request):
#     varfd = await request.json()
#     print( varfd)
#     return('sarower')

# @router.post('/login-check')
# def login_check(request:schemas.Login, db: Session = Depends(get_db)):
    
    
#     user = db.query(models.User).filter(models.User.email == request.email).first()
#     print(user)
#     if not user:
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail="User not found.")
#     if not Hash.verify_password(request.password,user.password):
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail="Incorrect password.")

#     access_token = JWTtoken.create_access_token(data={'sub':user.email})
#     return {'access_token':,'token_type':'bearer'}
