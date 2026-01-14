from pydantic import BaseModel, EmailStr, Field
from datetime import date
from typing import Optional


class EmployeeBase(BaseModel):
    """Base schema with common employee fields."""
    name: str = Field(..., min_length=1, max_length=100, description="Employee full name")
    email: EmailStr = Field(..., description="Employee email address")
    department: str = Field(..., min_length=1, max_length=50, description="Department name")
    designation: str = Field(..., min_length=1, max_length=100, description="Job designation")
    date_of_joining: date = Field(..., description="Date when employee joined")


class EmployeeCreate(EmployeeBase):
    """Schema for creating a new employee."""
    pass


class EmployeeUpdate(BaseModel):
    """Schema for updating an existing employee."""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    email: Optional[EmailStr] = None
    department: Optional[str] = Field(None, min_length=1, max_length=50)
    designation: Optional[str] = Field(None, min_length=1, max_length=100)
    date_of_joining: Optional[date] = None


class EmployeeResponse(EmployeeBase):
    """Schema for employee response (includes id)."""
    id: int

    class Config:
        from_attributes = True  # Allows conversion from SQLAlchemy model
