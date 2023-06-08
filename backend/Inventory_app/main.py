from fastapi import FastAPI,Depends
from pydantic import BaseModel
from . import models,schemas
from .routers import authentication,users
from .database import SessionLocal, engine
from pydantic import BaseModel
from .routers import oauth2


models.Base.metadata.create_all(bind=engine)

class Item(BaseModel):
    name: str
    description: str | None = None
    price: float


app = FastAPI()


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()



@app.post('/show/')
def show(request: Item, current_user: schemas.User = Depends(oauth2.get_current_user)):
    return request

app.include_router(authentication.router)
app.include_router(users.router)

