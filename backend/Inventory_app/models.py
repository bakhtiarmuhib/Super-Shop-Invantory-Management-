from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    user_role = Column(String)
    #photo

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String)

class Brand(Base):
    __tablename__ = 'brand'

    id = Column(Integer,primary_key=True,index=True)
    brand_name = Column(String)


class Product_attribute(Base):
    __tablename__  = 'product_attribute'

    id = Column(Integer,primary_key=True,index=True)
    attibute_name =  Column(String) 
    attibute_value = Column(String)


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, index=True)
    product_code = Column(String)
    #category
    #brand 
    stock = Column(Integer)
    sales_price = Column(Integer)
    purchase_cost = Column(Integer)
    #attributes


class Sales(Base):
    __tablename__ = 'Sales'

    #Product
    unit = Column(Integer)
    price = Column(Integer)
    customer_phone_number = Column(String)

class Damage(Base):
    __tablename__ = 'damage'

    #product
    unit = Column(Integer)
    cause = Column(String)
    

