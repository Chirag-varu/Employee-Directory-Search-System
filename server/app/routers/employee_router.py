from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from app.database.connection import get_db
from app.services.employee_service import EmployeeService
from app.schemas.employee import EmployeeResponse, EmployeeCreate
from app.exceptions.custom_exceptions import DatabaseConnectionError, ValidationError

router = APIRouter()


@router.get("/employees", response_model=List[EmployeeResponse])
def search_employees(
    search: Optional[str] = Query(
        None,
        max_length=100,
        description="Search term for employee name or department. If empty, returns all employees."
    ),
    limit: int = Query(default=50, ge=1, le=100, description="Maximum number of results"),
    offset: int = Query(default=0, ge=0, description="Number of results to skip"),
    db: Session = Depends(get_db)
):
    """
    Search employees by name or department.
    
    - **search**: Optional search term (searches both name and department)
    - **limit**: Maximum number of results to return (1-100, default 50)
    - **offset**: Number of results to skip for pagination
    
    Returns a list of employees matching the search criteria.
    """
    try:
        service = EmployeeService(db)
        employees = service.search_employees(search=search, limit=limit, offset=offset)
        return employees
    except DatabaseConnectionError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")


@router.get("/employees/{employee_id}", response_model=EmployeeResponse)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    """
    Get a specific employee by ID.
    """
    try:
        service = EmployeeService(db)
        employee = service.get_employee_by_id(employee_id)
        if not employee:
            raise HTTPException(status_code=404, detail="Employee not found")
        return employee
    except HTTPException:
        raise
    except DatabaseConnectionError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")


@router.post("/employees", response_model=EmployeeResponse, status_code=201)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    """
    Create a new employee.
    """
    try:
        service = EmployeeService(db)
        return service.create_employee(employee)
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except DatabaseConnectionError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail="An unexpected error occurred")
