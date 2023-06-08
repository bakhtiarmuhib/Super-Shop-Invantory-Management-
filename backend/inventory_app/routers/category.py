from fastapi import APIRouter,Depends,HTTPException,status
from .. import schemas,database,models
from . import oauth2
from sqlalchemy.orm import Session

router = APIRouter(tags=['Category'])




@router.get('/category')
def get_category(db : Session = Depends(database.get_db), current_user:schemas.User = Depends(oauth2.get_current_user)):
    all_category = db.query(models.Category).all()
    if not all_category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail='No category found.')
    return all_category


@router.post('/create-category/')
def create_new_category(request : schemas.Create_category, db : Session = Depends(database.get_db), current_user:schemas.User = Depends(oauth2.get_current_user)):
    new_category = models.Category(category_name=request.category_name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return {'detail': 'Category created'}


@router.put('/update-category/{id}')
def update_category(id : int,request : schemas.Create_category ,db : Session = Depends(database.get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    update_category_in_database = db.query(models.Category).filter(models.Category.id == id).first()
    if not update_category_in_database:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Category Not Found')
    db.query(models.Category).filter(models.Category.id == id).update({'category_name':request.category_name})
    return {'detail': 'Category Updated'}


@router.delete('/delete-category/{id}')
def update_category(id : int, db : Session = Depends(database.get_db), current_user : schemas.User = Depends(oauth2.get_current_user)):
    get_category = db.query(models.Category).filter(models.Category.id == id).first()
    if not get_category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No category for delete.')
    db.query(models.Category).filter(models.Category.id == id).delete(synchronize_session=False)
    db.commit()
    return {'detail': 'Category Deleted'}



