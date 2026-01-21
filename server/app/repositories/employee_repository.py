from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import List, Optional

from app.database.models import Employee
from app.schemas.employee import EmployeeCreate


class EmployeeRepository:
    """
    Repository layer for database operations on Employee model.
    Encapsulates all database queries and operations.
    """

    def __init__(self, db: Session):
        self.db = db

    def search(
        self,
        search: Optional[str] = None,
        limit: int = 50,
        offset: int = 0
    ) -> List[Employee]:
        """
        Search employees by name or department.
        
        Search is performed using LIKE with wildcards for partial matching.
        The query is optimized by:
        1. Using indexed columns (name, department)
        2. Limiting results to prevent large data transfers
        3. Using offset for pagination
        """
        keywords = search.lower().split() if search else []
        query = self.db.query(Employee)
        for kw in keywords:
            query = query.filter(
                or_(
                    Employee.name.ilike(f"%{kw}%"),
                    Employee.department.ilike(f"%{kw}%")
                )
            )
    
        return query.order_by(Employee.name).offset(offset).limit(limit).all()

    def get_by_id(self, employee_id: int) -> Optional[Employee]:
        """
        Get an employee by their ID.
        """
        return self.db.query(Employee).filter(Employee.id == employee_id).first()

    def get_by_email(self, email: str) -> Optional[Employee]:
        """
        Get an employee by their email address.
        """
        return self.db.query(Employee).filter(Employee.email == email).first()

    def create(self, employee_data: EmployeeCreate) -> Employee:
        """
        Create a new employee record.
        """
        db_employee = Employee(
            name=employee_data.name,
            email=employee_data.email,
            department=employee_data.department,
            designation=employee_data.designation,
            date_of_joining=employee_data.date_of_joining
        )
        self.db.add(db_employee)
        self.db.commit()
        self.db.refresh(db_employee)
        return db_employee

    def get_all(self, limit: int = 100, offset: int = 0) -> List[Employee]:
        """
        Get all employees with pagination.
        """
        return self.db.query(Employee).offset(offset).limit(limit).all()
