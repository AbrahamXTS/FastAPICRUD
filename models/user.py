from typing import Optional
from pydantic import BaseModel

class UserModel(BaseModel):
    id: Optional[str]
    name: str
    email: str
    password: str