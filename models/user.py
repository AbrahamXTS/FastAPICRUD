from typing import Optional
from pydantic import BaseModel

class UserModel(BaseModel):
    id: Optional[str]
    name: str
    email: str
    password: str

class UserEditedModel(BaseModel):
    id: Optional[str]
    name: Optional[str]
    email: Optional[str]
    password: Optional[str]