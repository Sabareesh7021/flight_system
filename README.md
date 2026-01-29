# Novidus – Django Flight Routes System

## Overview
**Novidus** is a Django-based **Flight Routes System** developed as part of a machine test.
The application represents airport routes as connected nodes and provides utilities to traverse routes, analyze durations, and manage airport route data through both UI and admin interfaces. The application is served using unicorn ASGI HTTP server and is compatible with Docker & Docker Swarm deployment.

---

## Features
- Add Airport Routes with airport code, position, and duration
- Find the **last reachable airport node** in a selected direction (Left / Right)
- Display the **airport with the longest duration**
- Display the **airport with the shortest duration** across the entire route
- Django Admin panel support
- Docker & Docker Swarm compatible deployment

---

## Tech Stack
- Python
- Django
- unicorn (ASGI HTTP Server)
- HTML (Django Templates)
- MySQL
- Docker & Docker Swarm

---

## Project Structure
```
flight_system/
├── .env.example
├── .env
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── manage.py
├── flight_system/
│   ├── __init__.py
│   ├── asgi.py
│   ├── config.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── routes/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── migrations/
└── templates/
    └── routes/
        ├── add_route.html
        ├── home.html
        ├── results.html
        └── search_route.html
```

---

## Environment Configuration

### .env.example
```env
DEBUG=True
SECRET_KEY=django-secret-key-change-me
ALLOWED_HOSTS=127.0.0.1,localhost

DB_NAME=novidus_db
DB_USER=novidus_user
DB_PASSWORD=novidus_password
DB_HOST=localhost
DB_PORT=3306
```

### Create .env
```bash
cp .env.example .env
```

---

## Local Setup

### 1. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Environment
```bash
cp .env.example .env
# Edit .env with your database credentials
```

### 4. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser
```bash
python manage.py createsuperuser
```
### 6. Create Static Files
```bash
python manage.py collectstatic
```

### 7. Start Development Server
```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000/`

---

## Docker Setup

### Build Docker Image
```bash
docker build -t flight_system:latest .
```

### Deploy with Docker Swarm
```bash
docker stack deploy -c docker-compose.yml novidus_stack
```



### Run Django Commands Inside Container
```bash
docker exec -it <container_id> python manage.py makemigrations
docker exec -it <container_id> python manage.py migrate
docker exec -it <container_id> python manage.py createsuperuser
```


---

## Application Logic

### Airport Route Model
Each airport node stores:
- **Airport Code**: Unique identifier for the airport
- **Position**: Node position in the route chain
- **Distance**: Travel time/distance to this airport
- **Connected airport Reference**: Link to the next airport

### Search Last Reachable Node
User interaction:
1. Select a starting airport
2. Choose a direction (Left / Right)
3. System traverses the route chain until no further node exists
4. Returns the last reachable airport in the selected direction

### Duration Analysis
- **Longest Duration**: Returns the airport with `MAX(duration)` across all routes
- **Shortest Duration**: Returns the airport with `MIN(duration)` across all routes

---

## Application Screens
- **Home**: Main landing page
- **Add Route**: Interface to add new airport routes
- **Search Route**: Interface to search and traverse routes
- **Results**: Display search results and route information

---

## Database Schema

### Airport Route Model
```
- id (Primary Key)
- airport_code (CharField)
- position (Choices)
- distance (Integer)
- connected_airport (ForeignKey - self reference)
```

---

## Admin Panel
Access Django Admin at `http://127.0.0.1:8000/admin/` with superuser credentials to:
- Manage airport routes
- View and edit node relationships
- Monitor durations

---

## Author
Sabareesh S

