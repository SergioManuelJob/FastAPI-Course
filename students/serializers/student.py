from typing import Optional
from pydantic import BaseModel, Field

class Student(BaseModel):
    id: Optional[int]
    name: Optional[str]
    age: int = Field(..., le=18, gt=0)

    class Config:
        orm_mode = True