from fastapi import APIRouter

router = APIRouter(tags=['Product'])



router.post('/create-product')
def create_product():
    return "create product"
