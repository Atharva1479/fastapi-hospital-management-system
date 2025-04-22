# 🏥 FastAPI Hospital Management System

A **secure**, **scalable**, and **Dockerized** Hospital Management System (HMS) backend built with **FastAPI**, **PostgreSQL**, and **JWT authentication**. This system provides a robust architecture for managing hospital functionalities like **patient registration**, **doctor profile management**, **appointment scheduling**, and **admin-level analytics**.

It supports **role-based access control** and is designed for scalability, making it ideal for integration with a frontend dashboard, mobile app, or third-party healthcare platforms. Now fully containerized using **Docker & Docker Compose**, making deployment and scaling effortless across environments.

---

## 🚀 Features

### 🔐 Authentication
- JWT-based login system
- Role-based access control (Patient, Doctor, Admin)
- Passwords hashed using Bcrypt

### 👩‍⚕️ User Roles
- **Patients**: Register, log in, book appointments, view appointment history
- **Doctors**: Log in, manage their availability and appointments
- **Admins**: Manage users, view system stats and appointment analytics

### 📅 Appointment Management
- Book appointments with available doctors
- Filter doctors by specialization and city
- View, update, or cancel appointments (based on roles)

### 📊 Admin Dashboard
- View total patients, doctors, and appointments
- Daily appointment trends
- Appointment count per doctor

### 🐳 Dockerized Deployment
- Easily run the entire project using `docker-compose`
- Built-in PostgreSQL container for database
- Environment-isolated and production-ready setup

---

## 🧱 Tech Stack

| Layer         | Technology                |
|---------------|---------------------------|
| Backend       | FastAPI                   |
| ORM           | SQLAlchemy                |
| Database      | PostgreSQL (Dockerized)   |
| Authentication| JWT (python-jose)         |
| Password Hash | Passlib (bcrypt)          |
| Migrations    | Alembic (optional)        |
| Environment   | Docker & Docker Compose   |
| Date Parsing  | python-dateutil           |
---

## 📁 Project Structure

```
hospital_management/
├── app/
│   ├── main.py               # Entry point
│   ├── models.py             # SQLAlchemy models
│   ├── schemas.py            # Pydantic schemas
│   ├── database.py           # DB connection and session
│   ├── auth.py               # JWT Auth logic
│   ├── services/             # Business logic
│   ├── routers/              # Route handlers
├── .env                      # Env variables
├── requirements.txt          # Python dependencies
├── Dockerfile                # App Docker config
├── docker-compose.yml        # Docker multi-service config
├── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repo
```bash
git clone https://github.com/Atharva1479/fastapi-hospital-management-system.git
cd fastapi-hospital-management-system
```

### 2️⃣ Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Setup PostgreSQL
- Create a database named `hospital_db`
- Update `.env` file with your DB credentials:

```env
DATABASE_URL=postgresql://username:password@localhost/hospital_db
SECRET_KEY=your_jwt_secret
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5️⃣ Run the Server
```bash
uvicorn app.main:app --reload
```

## 🐳 Dockerized Setup (Recommended)

### 📦 Prerequisites
- Install [Docker Desktop](https://www.docker.com/products/docker-desktop)
- Ensure `docker` and `docker-compose` work from the terminal

### 🚀 Run with Docker Compose
```bash
docker-compose up --build
```

📌 This will:
- Build the FastAPI app container
- Start a PostgreSQL container pre-configured with `hospital_db`
- Mount source files and expose API at [http://localhost:8000/docs](http://localhost:8000/docs)

---

## ✅ API Modules

| Module       | Description                         |
|--------------|-------------------------------------|
| `/auth`      | Login and token generation          |
| `/users`     | Registration and profile access     |
| `/doctors`   | Manage doctor profile and schedule  |
| `/patients`  | Manage patient profile & actions    |
| `/appointments` | Book, cancel, update appointments |
| `/admin`     | System analytics and insights       |

---

## 📌 Future Enhancements

- React-based Frontend UI
- Email notifications for appointments
- PDF report downloads for admin
- Integration with calendar APIs
