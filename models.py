from pydantic import BaseModel
from typing import Dict

class Student(BaseModel):
    name: str
    age: int
    gender: str
    marks: Dict[str, int]
    qualification: str
    course: str
