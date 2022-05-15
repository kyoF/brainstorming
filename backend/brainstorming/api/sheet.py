from fastapi import APIRouter

router = APIRouter()


@router.get('/sheets')
def get_sheets():
    pass


@router.post('/sheet/{sheet_id}')
def create_sheet():
    pass


@router.get('/sheet/{sheet_id}')
def get_sheet():
    pass


@router.delete('/sheet/{sheet_id}')
def delete_sheet():
    pass
