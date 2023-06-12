from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,Table
from sqlalchemy.orm import relationship

from .database import Base


# product_and_brand_association_tabel = Table(
#     'associate_between_band_product',
#     Base.metadata,
#     Column('brand_id',ForeignKey('brands.id')),
#     Column('product_id',ForeignKey('products.id')),
# )

product_and_attribute_association_tabel = Table(
    'associate_between_attribute_product',
    Base.metadata,
    Column('attribute_id',ForeignKey('product_attribute.id')),
    Column('product_id',ForeignKey('products.id')),
)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    user_role = Column(String)
    password = Column(String)
    #photo
    #sale
    
    sale = relationship('Sale',back_populates='saller',uselist=False)

class Category(Base):
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, index=True)
    category_name = Column(String)
    product = relationship('Product', back_populates='category',uselist=False)


class Brand(Base):
    __tablename__ = 'brands'

    id = Column(Integer,primary_key=True,index=True)
    brand_name = Column(String)

    
    product_brand  = relationship('Product', back_populates='brand',uselist=False)


class Product_attribute(Base):
    __tablename__  = 'product_attribute'

    id = Column(Integer,primary_key=True,index=True)
    attibute_name =  Column(String) 
    attibute_value = Column(String)

    #product
    attribute_in_product  = relationship('Product', secondary=product_and_attribute_association_tabel, back_populates='product_attribute')



class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String)
    product_code = Column(String)
    stock = Column(Integer)
    sales_price = Column(Integer)
    purchase_cost = Column(Integer)
    unit = Column(String,nullable=True)
    #attributes
    product_attribute  = relationship('Product_attribute', secondary=product_and_attribute_association_tabel, back_populates='attribute_in_product')
    #category
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category',back_populates='product')
    #brand 
    brand_id = Column(Integer, ForeignKey('brands.id'))
    brand  = relationship('Brand', back_populates='product_brand')
    #sales
    
    



class Sale(Base):
    __tablename__ = 'sales'

    id = Column(Integer, primary_key=True, index=True)
    unit = Column(Integer)
    price = Column(Integer)
    customer_phone_number = Column(String)
    
    #Product
    
    #user
    saller_id = Column(Integer , ForeignKey('user.id'))
    saller = relationship('User',back_populates='sale')

    

# class Damage(Base):
#     __tablename__ = 'damage'

#     id = Column(Integer, primary_key=True, index=True)
#     #product
#     unit = Column(Integer)
#     cause = Column(String)

# class Return(Base):
#     __tablename__ = 'returns'

#     id = Column(Integer, primary_key=True, index=True)
#     #product
#     unit = Column(Integer)
#     cause = Column(String)
    

