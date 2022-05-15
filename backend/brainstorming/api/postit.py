from brainstorming.schemas.Postit import Postit
from fastapi import APIRouter

router = APIRouter()


@router.post('/postit/{postit_id}')
def create_postit():
    pass


@router.get('/postit/{postit_id}')
def get_postit():
    pass


@router.post('/postit/{postit_id}')
def update_postit():
    pass


@router.delete('/postit/{postit_id}')
def delete_postit():
    pass
