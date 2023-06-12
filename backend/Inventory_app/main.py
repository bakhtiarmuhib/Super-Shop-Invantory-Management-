from fastapi import FastAPI,Depends
from pydantic import BaseModel
from . import models,schemas
from .routers import authentication,users,oauth2,category,product,attribute,brand,sale
from .database import SessionLocal, engine
from pydantic import BaseModel



models.Base.metadata.create_all(bind=engine)


app = FastAPI()



app.include_router(authentication.router)
app.include_router(users.router)
app.include_router(category.router)
app.include_router(attribute.router)
app.include_router(brand.router)
app.include_router(product.router)
app.include_router(sale.router)

