from pydantic import BaseModel, Field


class UserBase(BaseModel):
    login_id: str = Field(None, description="ログインID")
    name: str = Field(None, description="名前")


class User(UserBase):
    id: int


class UserCreateRequest(UserBase):
    password: str = Field(None, description="パスワード")
