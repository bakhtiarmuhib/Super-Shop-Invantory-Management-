from fastapi import APIRouter,Depends,HTTPException,status
from .. import schemas,database,models
from . import oauth2
from sqlalchemy.orm import Session

router = APIRouter(tags=['Attribute'])




@router.get('/attribute',status_code=status.HTTP_200_OK)
def get_attribute(db : Session = Depends(database.get_db), current_user:schemas.User = Depends(oauth2.get_current_user)):
    all_attribute = db.query(models.Product_attribute).all()
    if not all_attribute:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail='No attribute found.')
    return all_attribute


@router.post('/create-attribute/',status_code=status.HTTP_201_CREATED)
def create_new_attribute(request : schemas.Create_Attribute, db : Session = Depends(database.get_db), current_user:schemas.User = Depends(oauth2.get_current_user)):
    new_attribute = models.Product_attribute(attibute_name=request.attibute_name, attibute_value= request.attibute_value)
    db.add(new_attribute)
    db.commit()
    db.refresh(new_attribute)
    return {'detail': 'Attribute created'}


@router.put('/update-attribute/{id}',status_code=status.HTTP_202_ACCEPTED)
def update_attribute(id : int,request : schemas.Create_Attribute ,db : Session = Depends(database.get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    update_attribute_in_database = db.query(models.Product_attribute).filter(models.Product_attribute.id == id)
    if not update_attribute_in_database:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Attribute Not Found')
    update_attribute_in_database.update(request.dict())
    db.commit()
    return {'detail': 'Attribute Updated'}


@router.delete('/delete-attribute/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_attribute(id : int, db : Session = Depends(database.get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    get_attribute = db.query(models.Product_attribute).filter(models.Product_attribute.id == id)
    if not get_attribute:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No attribute for delete.')
    get_attribute.delete(synchronize_session=False)
    db.commit()
    return {'detail': 'Attribute Deleted'}



