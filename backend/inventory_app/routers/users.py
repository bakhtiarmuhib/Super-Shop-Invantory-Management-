from fastapi import APIRouter,Depends,HTTPException,status
from ..import schemas , models,hashing
from . import oauth2
from sqlalchemy.orm import Session
from ..database import SessionLocal
router = APIRouter(tags=['User'])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@router.post('/create-user/')
def create_new_user(request:schemas.User, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    print(user)
    if user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail="User Email Already Taken")
    create_user = models.User(first_name = request.first_name, last_name = request.last_name,user_role = request.user_role, email = request.email,password = hashing.Hash.bcrypt(request.password))
    db.add(create_user)
    db.commit()
    db.refresh(create_user)
    return {'detail': 'User Created Successfully'}


@router.put('/update-user/{id}')
def update_use(id, request: schemas.Update_User ,db: Session = Depends(get_db),current_user : schemas.User = Depends(oauth2.get_current_user)):
    user_for_update = db.query(models.User).filter(models.User.id == id)
    if not user_for_update:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No user found for update')
    user_for_update.update(request.dict())
    db.commit()
    return {'detail' : 'User updated successfully.'}
    

# @router.update('/change-password/{id}')
# def update_use(request: schemas.Update_User ,db: Session = Depends(get_db),current_user : schemas.User = Depends(oauth2.get_current_user)):
#     user_for_update = db.query(models.User).filter(models.User.id == id)
#     if not user_for_update:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No user found for update')
#     user_for_update.update(request.dict())
#     db.commit()
#     return {'detail' : 'User updated successfully.'}
