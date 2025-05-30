from pydantic import BaseModel, Field
from typing import Optional, List, Dict

# Todo: Create the Employee model with the id, name, email, and department fields
class Employee(BaseModel):
    id: int
    name: str = Field(..., min_length=3, description="Name of the employee, must be at least 3 characters long")
    department: str = Field(default="General", description="Department of the employee, defaults to 'General'")
    salary: float = Field(..., ge=10000, description="Salary of the employee, must be greater than or equal to 10000")
    email: Optional[str] = Field(None, description="Optional email address")
    skills: List[str] = Field(default_factory=list, description="List of employee skills")
    metadata: Dict[str, str] = Field(default_factory=dict, description="Additional metadata")

user = Employee(
     id=1,
     name="John Doe",
     department="Engineering",
     salary=12000.0,
     email="john.doe@example.com",
     skills=["Python", "FastAPI"],
     metadata={"location": "Remote", "level": "Senior"}
)
print(user)