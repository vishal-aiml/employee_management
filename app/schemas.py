from pydantic import BaseModel

class EmployeeObject(BaseModel):
    name: str
    email: str
    department: str
    salary: float
    city: str

class EmployeeObjectResponse(EmployeeObject):
    id: int

    class Config:
        orm_mode = True