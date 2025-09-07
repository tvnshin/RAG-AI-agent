from pydantic import BaseModel

class UserOut(BaseModel):
    id: int
    name: str
    status: str

class UserFuncResponse(BaseModel):
    user_found: bool
    user: UserOut | None = None