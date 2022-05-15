from pydantic import BaseModel, Field


class SheetBase(BaseModel):
    sheet_id = Field(None, description='シートID')
    divide = Field(None, description='分割範囲')
    formula = Field(None, description='式')


class Postit(PostitBase):
    id: int
