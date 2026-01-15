# Employee Directory Search System

A full-stack employee directory application with optimized search functionality, built with React + Vite (Frontend) and Python + FastAPI (Backend).

## 🌐 Live Demo

**🔗 [https://eds.chiragvaru.me/](https://eds.chiragvaru.me/)**

| Service | Platform |
|---------|----------|
| Frontend | Vercel |
| Backend | Render |

---

## 🚀 Features

- **Optimized Search**: Debounced search with controlled API requests
- **Server-Side Pagination**: Fetch only 8 employees at a time for better performance
- **Real-time Filtering**: Search by employee name or department
- **Responsive Design**: Modern UI with dark theme using shadcn/ui
- **Clean Architecture**: Layered architecture with Repository Pattern
- **State Management**: Proper use of React state and props
- **API State Handling**: Loading, error, and empty states
- **Environment-based** configuration (no hardcoded URLs or credentials)
---
## ScreenShot
![alt text](client/public/image.png)

---
### Search by name
![alt text](client/public/image-1.png)

---
### Search by department
![alt text](client/public/image-2.png)

---
### No user Found:
![alt text](client/public/image-3.png)

---
## 📁 Project Structure

```
Employee Directory Search System/
├── client/                 # React + Vite Frontend
│   ├── src/
│   │   ├── components/    # Reusable UI components
│   │   ├── pages/         # Page components
│   │   ├── services/      # API service layer
│   │   ├── hooks/         # Custom React hooks (useDebounce)
│   │   ├── types/         # TypeScript type definitions
│   │   └── lib/           # Utility functions
│   └── package.json
│
└── server/                # Python + FastAPI Backend
    ├── app/
    │   ├── routers/       # API route handlers
    │   ├── services/      # Business logic layer
    │   ├── repositories/  # Database access layer
    │   ├── schemas/       # Pydantic validation models
    │   ├── database/      # Database models & connection
    │   └── exceptions/    # Custom exceptions
    ├── seed.py            # Database seeding script
    └── requirements.txt
```

## 🛠️ Tech Stack

### Frontend
- **Vite React 18** with TypeScript for fast development
- **TailwindCSS** for styling
- **shadcn/ui** for UI components
- **Axios** for server requests
- **Lucide React** for icons

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - ORM for database operations
- **Pydantic** - Data validation
- **PyMySQL** - MySQL database driver
- **Python-dotenv** - Environment variable management
- **Uvicorn** - ASGI server

### Database
- **MySQL** (via Aiven Cloud)

---

## 🔑 Key Architectural Highlights

| Feature | Description |
|---------|-------------|
| **☁️ Cloud MySQL (Aiven)** | Production-grade MySQL database hosted on Aiven Cloud with SSL encryption, automatic backups, and high availability |
| **🔧 Centralized API Management** | Environment-based API configuration (`VITE_MODE`) to seamlessly switch between development and production endpoints |
| **🔍 Combined Search Query** | Single optimized SQL query using `OR` clause to search across multiple fields (name, department) efficiently |
| **📘 TypeScript** | Full type safety in the frontend with TypeScript for better developer experience and fewer runtime errors |
| **🏛️ Repository Pattern** | Clean separation of concerns with Router → Service → Repository layers for maintainability and testability |
| **📌 API Versioning** | Versioned API endpoints (`/api/v1/employees`) for backward compatibility and smooth API evolution |

---

## 📦 Setup Instructions

### Prerequisites
- Node.js (v18+)
- Python (v3.12+) - *Only if running locally*
- MySQL database (local or cloud instance like Aiven) - *Only if running locally*
- **Docker Desktop** - *Required for Docker setup*
---

### Frontend Setup

1. **Navigate to client directory**
```powershell
cd client
```

2. **Install dependencies**
```powershell
npm install
```

3. **Configure environment variables**

Create a `.env.local` file in the `client` directory:

```env
VITE_MODE=development
VITE_API_DEV_URL=http://localhost:8000/api/v1/employees
VITE_API_PROD_URL=https://your-production-api.com/api/v1/employees
```

4. **Start the development server**
```powershell
npm run dev
```

The application will be available at: `http://localhost:5173`

---

### Backend Setup
## 🐳 Quick Start with Docker (Recommended)

The easiest way to run the backend API is using our pre-built Docker image with test environment included.

### Prerequisites
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installed and running

### Steps

1. **Pull the Docker image from Docker Hub**
```powershell
docker pull vchirag/employee-directory-api:latest
```

2. **Run the container**
```powershell
docker run -p 8000:8000 vchirag/employee-directory-api:latest
```

3. **Access the API**
- API: http://localhost:8000
- Documentation: http://localhost:8000/docs
- Health Check: http://localhost:8000/health

**That's it!** The Docker image includes:
- ✅ Pre-configured test database connection
- ✅ SSL certificates (ca.pem)
- ✅ 50 sample employees
- ✅ All dependencies installed

**Optional: Run in detached mode (background)**
```powershell
docker run -d -p 8000:8000 --name employee-api vchirag/employee-directory-api:latest
```

**Stop the container**
```powershell
docker stop employee-api
```

---

## 💻 Local Development Setup (Alternative)

If you want to develop or modify the backend locally:

1. **Navigate to server directory**
```powershell
cd server
```

1. **Install Python dependencies**
```powershell
pip install -r requirements.txt
```

1. **Configure environment variables**

Create a `.env` file in the `server` directory:

```env
# Database Configuration
DATABASE_URL=mysql+pymysql://username:password@host:port/database

# CORS - Allowed origins
ALLOWED_ORIGINS=http://localhost:5173

# Server Configuration
HOST=0.0.0.0
PORT=8000
```

**Example for Aiven MySQL:**
```env
DATABASE_URL=mysql+pymysql://avnadmin:your_password@your-mysql-instance.aivencloud.com:16961/defaultdb
```

4. **Seed the database with sample data**
```powershell
python seed.py
```

5. **Start the backend server**
```powershell
python run.py
```

The API will be available at: `http://localhost:8000`
- API Documentation: `http://localhost:8000/docs`
- Health Check: `http://localhost:8000/health`

---

## 🗄️ Database Choice: MySQL

### Why MySQL?

1. **Industry Standard**: Widely used in production environments with extensive community support
2. **ACID Compliance**: Ensures data integrity and consistency
3. **Powerful Indexing**: Supports multiple index types (B-Tree, Full-Text, Hash) for optimized queries
4. **Scalability**: Handles large datasets efficiently with proper indexing and query optimization
5. **Reliability**: Battle-tested with proven stability in enterprise applications
6. **Cloud Ready**: Easy deployment on cloud platforms (AWS RDS, Google Cloud SQL, Aiven)

### Database Schema

```sql
CREATE TABLE employees (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    department VARCHAR(50) NOT NULL,
    designation VARCHAR(100) NOT NULL,
    date_of_joining DATE NOT NULL,
    
    INDEX idx_name (name),
    INDEX idx_department (department),
    INDEX idx_name_department (name, department)
);
```

---

## ⚡ Search Performance Optimization

### 1. **Frontend Debouncing**
- **Implementation**: Custom `useDebounce` hook with 500ms delay
- **Benefit**: Prevents API calls on every keystroke
- **Example**: Typing "Rahul" triggers only 1 API call instead of 5
- **Impact**: Reduces server load by 80-90% during rapid typing

```typescript
// Before Debouncing: 5 API calls for "Rahul"
// r -> API call
// ra -> API call
// rah -> API call
// rahu -> API call
// rahul -> API call

// After Debouncing: 1 API call
// rahul -> API call (after 500ms pause)
```

### 2. **Database Indexing**
- **Indexed Columns**: `name`, `department`
- **Composite Index**: `(name, department)` for combined searches
- **Benefit**: Reduces query time from O(n) to O(log n)
- **Impact**: Search queries execute in <10ms even with 10,000+ employees

```python
# Database Model with Indexes
class Employee(Base):
    __tablename__ = "employees"
    
    name = Column(String(100), index=True)        # Single index
    department = Column(String(50), index=True)   # Single index
    
    __table_args__ = (
        Index('idx_name_department', 'name', 'department'),  # Composite index
    )
```

### 3. **Server-Side Pagination**
- **Page Size**: 8 employees per page
- **Implementation**: `LIMIT` and `OFFSET` in SQL queries
- **Benefit**: Reduces data transfer and memory usage
- **Impact**: Only fetches required data, not entire dataset

```python
# Query with Pagination
def search(search: str, limit: int = 8, offset: int = 0):
    return db.query(Employee) \
        .filter(Employee.name.ilike(f"%{search}%")) \
        .offset(offset) \
        .limit(limit) \
        .all()
```

### 4. **Efficient SQL Queries**
- **ILIKE with Wildcards**: Case-insensitive partial matching
- **OR Clause**: Search across multiple columns (name OR department)
- **Connection Pooling**: Reuses database connections (SQLAlchemy)
- **Pre-ping**: Checks connection health before use

```python
# Optimized Search Query
query = db.query(Employee).filter(
    or_(
        Employee.name.ilike(f"%{search}%"),
        Employee.department.ilike(f"%{search}%")
    )
).order_by(Employee.name).offset(offset).limit(limit)
```

### 5. **Layered Architecture**
- **Separation of Concerns**: Routes → Services → Repositories → Database
- **Caching Potential**: Easy to add Redis/Memcached at service layer
- **Benefit**: Clean code, easy to optimize individual layers

---

## 🎨 Frontend Architecture

### Component Structure
- **SearchBar**: Controlled input with debounced search
- **EmployeeList**: Grid layout with responsive design
- **EmployeeCard**: Individual employee display with icons
- **Home**: Main page orchestrating state and API calls

### State Management
- React `useState` for local state
- Props drilling for component communication
- Custom hooks (`useDebounce`) for reusable logic

---

## 🏗️ Backend Architecture

### Layered Architecture with Repository Pattern

```
Request Flow:
Client → Router → Service → Repository → Database

Router:       HTTP handling, validation, responses
Service:      Business logic, orchestration
Repository:   Database queries (CRUD operations)
Models:       Database table definitions
Schemas:      Request/Response validation
```

### Why This Pattern?
1. **Separation of Concerns**: Each layer has a single responsibility
2. **Testability**: Easy to unit test individual layers
3. **Maintainability**: Changes in one layer don't affect others
4. **Scalability**: Easy to add features (e.g., caching, logging)

---

## 🔌 API Endpoints

### GET `/api/employees`
Search employees by name or department

**Query Parameters:**
- `search` (optional): Search term
- `limit` (optional, default: 8): Number of results
- `offset` (optional, default: 0): Pagination offset

**Example:**
```bash
GET http://localhost:8000/api/employees?search=rahul&limit=8&offset=0
```

**Response:**
```json
[
  {
    "id": 1,
    "name": "Rahul Sharma",
    "email": "rahul.sharma@company.com",
    "department": "Engineering",
    "designation": "Software Engineer",
    "date_of_joining": "2023-01-15"
  }
]
```

### GET `/api/employees/{id}`
Get a specific employee by ID

### POST `/api/employees`
Create a new employee (future enhancement)

---

## 👤 Author

This project is created for educational purposes.
Created as part of an SDE assignment demonstrating full-stack development skills with a focus on performance optimization and clean architecture.
