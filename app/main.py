from fastapi import FastAPI
from app import models, database
from app.routers import auth_routes
from app.routers import doctor_routes
from app.routers import patient_routes, search_routes, appointment_routes, admin_routes

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

app.include_router(auth_routes.router)
app.include_router(doctor_routes.router)
app.include_router(patient_routes.router)
app.include_router(search_routes.router)
app.include_router(appointment_routes.router)
app.include_router(admin_routes.router)

@app.get("/")
def home():
    return {"message": "Welcome to Doctor Booking API"}
