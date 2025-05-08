from pydantic import BaseModel, EmailStr, ConfigDict


class UserBase(BaseModel):
    username: str
    email: EmailStr

    # Pydantic v2: включаем «ORM-режим» через from_attributes
    model_config = ConfigDict(from_attributes=True)


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
