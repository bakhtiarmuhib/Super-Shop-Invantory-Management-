from fastapi import HTTPException,status,Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from . import JWTtoken
from .. import schemas

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return JWTtoken.verify_token(token,credentials_exception)
    
    
