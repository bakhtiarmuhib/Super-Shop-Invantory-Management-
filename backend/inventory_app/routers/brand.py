from fastapi import APIRouter,Depends,HTTPException,status
from .. import schemas,database,models
from . import oauth2,JWTtoken
from sqlalchemy.orm import Session

router = APIRouter(tags=['Brand'])




@router.get('/brand',status_code=status.HTTP_200_OK)
def get_brand(db : Session = Depends(database.get_db), current_user:schemas.User = Depends(oauth2.get_current_user),current_active_user :schemas.Show_User = Depends(oauth2.get_current_active_user)):
    print('current')
    print()
    all_brand = db.query(models.Brand).all()
    if not all_brand:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail='Brand data not found.')
    return all_brand


@router.post('/create-brand/',status_code=status.HTTP_201_CREATED)
def create_new_brand(request : schemas.Create_Brand, db : Session = Depends(database.get_db), current_user:schemas.User = Depends(oauth2.get_current_user)):
    new_brand = models.Brand(brand_name=request.brand_name)
    db.add(new_brand)
    db.commit()
    db.refresh(new_brand)
    return {'detail': 'Attribute created'}


@router.put('/update-brand/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_brand(id : int,request : schemas.Create_Brand ,db : Session = Depends(database.get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    update_brand_in_database = db.query(models.Brand).filter(models.Brand.id == id)
    if not update_brand_in_database:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Brand not found from update')
    update_brand_in_database.update(request.dict())
    db.commit()
    return {'detail': 'Brand Updated'}


@router.delete('/delete-brand/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_brand(id : int, db : Session = Depends(database.get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    get_brand = db.query(models.Brand).filter(models.Brand.id == id)
    if not get_brand:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No Brand for delete.')
    get_brand.delete()
    db.commit()
    return {'detail': 'Brand Deleted'}



