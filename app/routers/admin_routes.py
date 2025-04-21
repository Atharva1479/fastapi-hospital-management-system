from fastapi import APIRouter, Depends, HTTPException
from app import models, schemas, database, auth
from app.services import admin_service
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(prefix="/admin", tags=["Admin"])

@router.get("/doctors", response_model=List[schemas.AdminDoctorResponse])
def get_doctors(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    if current_user.role != "ADMIN":
        raise HTTPException(status_code=403, detail="Only admins can access this")

    return admin_service.get_all_doctors(db)

@router.get("/patients", response_model=List[schemas.AdminPatientResponse])
def get_patients(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    if current_user.role != "ADMIN":
        raise HTTPException(status_code=403, detail="Only admins can access this")

    return admin_service.get_all_patients(db)

@router.get("/appointments", response_model=List[schemas.AdminAppointmentResponse])
def get_appointments(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    if current_user.role != "ADMIN":
        raise HTTPException(status_code=403, detail="Only admins can access this")

    return admin_service.get_all_appointments(db)

@router.put("/doctor/{doctor_id}/status", response_model=schemas.AdminDoctorResponse)
def toggle_doctor_status(
    doctor_id: int,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    if current_user.role != "ADMIN":
        raise HTTPException(status_code=403, detail="Only admins can update this")

    doctor = admin_service.toggle_doctor_status(db, doctor_id)
    return schemas.AdminDoctorResponse(
        id=doctor.id,
        full_name=doctor.user.full_name,
        email=doctor.user.email,
        specialization=doctor.specialization,
        city=doctor.city,
        is_active=doctor.is_active
    )

@router.get("/stats", response_model=schemas.SystemStats)
def get_system_stats(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    if current_user.role != "ADMIN":
        raise HTTPException(status_code=403, detail="Unauthorized")
    return admin_service.get_system_stats(db)

@router.get("/appointments/doctor", response_model=List[schemas.AppointmentCountPerDoctor])
def get_appointments_per_doctor(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    if current_user.role != "ADMIN":
        raise HTTPException(status_code=403, detail="Unauthorized")
    return admin_service.get_appointment_count_per_doctor(db)

@router.get("/appointments/trend", response_model=List[schemas.DailyAppointmentTrend])
def get_appointment_trend(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    if current_user.role != "ADMIN":
        raise HTTPException(status_code=403, detail="Unauthorized")
    return admin_service.get_daily_appointment_trend(db)
