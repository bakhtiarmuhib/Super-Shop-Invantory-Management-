from fastapi import APIRouter,Depends,HTTPException,status
from ..import schemas , models
from fastapi.security import OAuth2PasswordRequestForm
from ..hashing import Hash
from sqlalchemy.orm import Session
from ..database import SessionLocal
from . import JWTtoken

router = APIRouter(tags=['Authentication'])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/login')
def login(request:OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail="User not found.")
    if not Hash.verify_password(request.password,user.password):
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail="Incorrect password.")

    access_token = JWTtoken.create_access_token(data={'sub':user.email})
    return {'access_token':access_token,'token_type':'bearer'}

