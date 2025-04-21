# 🏥 FastAPI Hospital Management System

A secure, scalable, and role-based Hospital Management System (HMS) built using **FastAPI**, **PostgreSQL**, and **JWT authentication**. This backend application supports patient registration, doctor management, appointment scheduling, and admin analytics.

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

---

## 🧱 Tech Stack

| Layer        | Technology               |
|--------------|---------------------------|
| Backend      | FastAPI                   |
| ORM          | SQLAlchemy                |
| Database     | PostgreSQL                |
| Auth         | JWT (using python-jose)   |
| Passwords    | passlib (bcrypt)          |
| Migrations   | Alembic (optional)        |
| Date Parsing | python-dateutil           |

---

## 📁 Project Structure

```
hospital_management/
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── auth.py
│   ├── services/
│   ├── routers/
├── .env
├── requirements.txt
├── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repo
```bash
git clone https://github.com/yourusername/fastapi-hospital-management-system.git
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
- Docker support for deployment
- Integration with calendar APIs
