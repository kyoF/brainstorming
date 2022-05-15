from pydantic import BaseModel, Field


class PostitBase(BaseModel):
    postit_id = Field(None, description='付箋ID')
    title = Field(None, description='タイトル')
    remarks = Field(None, description='備考')
    xaxis = Field(None, description='X軸')
    yaxis = Field(None, description='Y軸')


class Postit(PostitBase):
    id: int


class PostitCreateRequest(PostitBase):
    sheet_id = Field(None, description='シートID')
