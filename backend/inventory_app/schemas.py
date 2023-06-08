from pydantic import BaseModel


class Login(BaseModel):
    email : str
    password : str


class User(BaseModel):
    first_name : str
    last_name : str
    email : str
    user_role : str
    password : str

class Create_category(BaseModel):
    category_name : str