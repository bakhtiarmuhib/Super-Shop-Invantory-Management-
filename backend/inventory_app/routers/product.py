from fastapi import APIRouter,Depends,HTTPException,status
from .. import schemas,database,models
from . import oauth2
from sqlalchemy.orm import Session
from uuid import uuid4
from typing import List

router = APIRouter(tags=['Product'])




@router.get('/product',response_model=List[schemas.Show_Product] ,status_code=status.HTTP_200_OK)
def get_product(db : Session = Depends(database.get_db), current_user:schemas.User = Depends(oauth2.get_current_user)):
    all_product = db.query(models.Product).all()
    print(current_user)
    if not all_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail='Product data not found.')
    return all_product


@router.post('/create-product/',status_code=status.HTTP_201_CREATED)
def create_new_product(request : schemas.Create_Product, db : Session = Depends(database.get_db), current_user:schemas.User = Depends(oauth2.get_current_user)):
    print(request)
    new_product = models.Product(product_name=request.product_name, stock=request.stock ,sales_price=request.sales_price, 
                                 purchase_cost=request.purchase_cost, category_id=request.category_id ,brand_id=request.brand_id ,unit=request.unit,product_code=str(uuid4()))
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return {'detail': 'product created'}


@router.put('/update-product/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_product(id : int,request : schemas.Create_Product ,db : Session = Depends(database.get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    update_product_in_database = db.query(models.Product).filter(models.Product.id == id)
    if not update_product_in_database:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Brand not found from update')
    update_product_in_database.update(request.dict())
    db.commit()
    return {'detail': 'product Updated sucessfully'}


@router.delete('/delete-product/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_product(id : int, db : Session = Depends(database.get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    get_product = db.query(models.Brand).filter(models.Brand.id == id)
    if not get_product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No product for delete.')
    get_product.delete()
    db.commit()
    return {'detail': 'Brand Deleted'}




