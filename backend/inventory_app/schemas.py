from typing import Optional,List
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


class Update_User(BaseModel):
    first_name : str
    last_name : str


class Create_category(BaseModel):
    category_name : str

class Show_Category(Create_category):
    class Config:
        orm_mode = True

class Create_Attribute(BaseModel):
    attibute_name : str
    attibute_value : str




class Create_Brand(BaseModel):
    brand_name : str

class Show_Brand(Create_Brand):
    class Config:
        orm_mode = True




class Create_Product(BaseModel):
    product_name : str
    stock : int
    sales_price : int
    purchase_cost : int
    category_id : int
    brand_id : int
    unit : Optional[str] = None

class Show_Product(Create_Product):
    product_code : str
    category : Show_Category
    brand : Show_Brand
    class Config:
        orm_mode = True

class Create_Sales(BaseModel):
    unit:int
    customer_phone_number : str
    product_id : int
    saller_id : int


 