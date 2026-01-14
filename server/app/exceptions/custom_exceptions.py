class DatabaseConnectionError(Exception):
    """Raised when database connection fails."""
    pass


class ValidationError(Exception):
    """Raised when validation fails."""
    pass


class EmployeeNotFoundError(Exception):
    """Raised when employee is not found."""
    pass
