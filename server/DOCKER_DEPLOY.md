# Docker Deployment Guide

## Running the Employee Directory API

### Prerequisites
- Docker installed on your machine
- MySQL database (local or cloud like Aiven, AWS RDS, etc.)

### Quick Start

**1. Pull the Docker image:**
```bash
docker pull YOUR_DOCKERHUB_USERNAME/employee-directory-api:latest
```

**2. Create a `.env` file with your database credentials:**
```env
DATABASE_URL=mysql+pymysql://username:password@host:port/database
ALLOWED_ORIGINS=http://localhost:5173
HOST=0.0.0.0
PORT=8000
```

**3. Run the container:**
```bash
docker run -p 8000:8000 --env-file .env YOUR_DOCKERHUB_USERNAME/employee-directory-api:latest
```

**4. (Optional) Seed the database:**
```bash
# Access the container
docker exec -it <container_id> bash

# Run seed script
python seed.py
```

### Alternative: Using Environment Variables Directly

```bash
docker run -p 8000:8000 \
  -e DATABASE_URL="mysql+pymysql://user:pass@host:port/db" \
  -e ALLOWED_ORIGINS="http://localhost:5173" \
  -e HOST="0.0.0.0" \
  -e PORT="8000" \
  YOUR_DOCKERHUB_USERNAME/employee-directory-api:latest
```

### Using Docker Compose

Create a `docker-compose.yml`:

```yaml
version: '3.8'

services:
  api:
    image: YOUR_DOCKERHUB_USERNAME/employee-directory-api:latest
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=mysql+pymysql://user:pass@host:port/db
      - ALLOWED_ORIGINS=http://localhost:5173
      - HOST=0.0.0.0
      - PORT=8000
    restart: unless-stopped
```

Then run:
```bash
docker-compose up -d
```

### Accessing the API

Once running, access:
- API: http://localhost:8000
- Documentation: http://localhost:8000/docs
- Health Check: http://localhost:8000/health

### Security Notes

⚠️ **Never commit `.env` files or credentials to Git**
⚠️ **Use strong passwords for production databases**
⚠️ **Configure CORS origins based on your frontend URL**
