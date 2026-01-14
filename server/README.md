# Backend - Employee Directory API

Simple FastAPI backend for employee search and management.

## 📁 Project Structure

```
app/
├── main.py              # App entry point (start here!)
├── routers/             # API endpoints (URLs)
├── services/            # Business logic
├── repositories/        # Database queries
├── database/            # Database setup & models
├── schemas/             # Data validation
└── exceptions/          # Error handling
```

## 🔄 How It Works

**Simple Flow:** Request → Router → Service → Repository → Database

1. **Router** - Receives HTTP requests at `/api/v1/employees`
2. **Service** - Processes the request (business logic)
3. **Repository** - Talks to the database
4. **Database** - Returns employee data

## � What Each Folder Does

### `routers/` - API Endpoints
Defines URLs like `/api/v1/employees` and handles requests.

### `services/` - Business Logic  
Processes data before sending to database (like validation, formatting).

### `repositories/` - Database Queries
Executes SQL queries to get/save data.

### `database/` - Database Setup
- `models.py` - Defines Employee table structure
- `connection.py` - Connects to MySQL database

### `schemas/` - Data Validation
Defines what data is required (like name, email must be present).

## 🚀 Quick Start

### Option 1: Using Docker (Easiest)

```bash
# Pull and run
docker pull vchirag/employee-directory-api:latest
docker run -p 8000:8000 vchirag/employee-directory-api:latest
```

Done! Go to http://localhost:8000/docs

### Option 2: Run Locally

```bash
# Install packages
pip install -r requirements.txt

# Create .env file with your database URL
# DATABASE_URL=mysql+pymysql://user:pass@host:port/database

# Add sample data
python seed.py

# Start server
python run.py
```

Go to http://localhost:8000/docs

## 🔌 Available APIs

| What | URL | Example |
|------|-----|----------|
| Search employees | `GET /api/v1/employees?search=john` | Find employees named "john" |
| Get one employee | `GET /api/v1/employees/1` | Get employee with ID 1 |
| Add new employee | `POST /api/v1/employees` | Create new employee |
| API docs | `GET /docs` | Interactive documentation |
| Health check | `GET /health` | Check if API is running |

## ✏️ Making Changes

### Adding a New API Endpoint

1. **Add to Router** (`routers/employee_router.py`) - Create the URL
2. **Add to Service** (`services/employee_service.py`) - Add logic  
3. **Add to Repository** (`repositories/employee_repository.py`) - Add database query
4. **Test** - Go to `/docs` and try it out!

### Modifying Search Logic

Edit `repositories/employee_repository.py` to change how search works.

### Adding Database Fields

Edit `database/models.py` to add new columns to Employee table.

## � Database

Employee table has:
- `id` - Unique number
- `name` - Employee name
- `email` - Email address
- `department` - Which department (Engineering, Marketing, etc.)
- `position` - Job title
- `joining_date` - When they joined

### Add Sample Data

Edit `seed.py` and run:
```bash
python seed.py
```

## 🧪 Testing APIs

Go to http://localhost:8000/docs for interactive testing!

Or use curl:
```bash
# Search
curl "http://localhost:8000/api/v1/employees?search=john"

# Get one
curl "http://localhost:8000/api/v1/employees/1"
```

## ⚙️ Configuration

**Environment Variables (.env file):**

| Variable | What it does | Example |
|----------|--------------|---------|
| `DATABASE_URL` | Where your database is | `mysql+pymysql://user:pass@host/db` |
| `ALLOWED_ORIGINS` | Which frontends can connect | `http://localhost:5173` |
| `PORT` | Which port to run on | `8000` |

## ❓ Common Issues

**Can't connect to database**
- Check `DATABASE_URL` in `.env` file
- Make sure MySQL is running

**Port already in use**
- Change `PORT` in `.env` to something else (like 8001)

**Missing packages**
```bash
pip install -r requirements.txt
```

## 📦 What's Installed

- **FastAPI** - Web framework  
- **SQLAlchemy** - Database tool
- **PyMySQL** - Connects to MySQL
- **Uvicorn** - Runs the server

## 📖 Learn More

- FastAPI Docs: https://fastapi.tiangolo.com/
- Go to `/docs` on your running server for interactive API documentation

---

**Need help?** Check the main README or `/docs` endpoint!
