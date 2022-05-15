from fastapi import APIRouter

router = APIRouter()


@router.post('/users')
def create_user():
    pass


@router.get('/user/{user_id}')
def get_user():
    pass
