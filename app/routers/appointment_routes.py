from fastapi import APIRouter, Depends, HTTPException
from app import models, schemas, database, auth
from app.services import appointment_service, patient_service, doctor_service
from sqlalchemy.orm import Session
from typing import List

router = APIRouter(prefix="/appointments", tags=["Appointments"])

@router.post("/", response_model=schemas.AppointmentResponse)
def book_appointment(
    data: schemas.AppointmentCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    if current_user.role != "PATIENT":
        raise HTTPException(status_code=403, detail="Only patients can book appointments")

    patient = patient_service.get_patient_profile(db, current_user)
    appointment = appointment_service.book_appointment(db, patient, data)
    return appointment

@router.get("/my", response_model=List[schemas.AppointmentResponse])
def get_patient_appointments(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    if current_user.role != "PATIENT":
        raise HTTPException(status_code=403, detail="Only patients can view this")

    patient = patient_service.get_patient_profile(db, current_user)
    return appointment_service.get_appointments_by_patient(db, patient.id)

@router.get("/doctor", response_model=List[schemas.AppointmentResponse])
def get_doctor_appointments(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    if current_user.role != "DOCTOR":
        raise HTTPException(status_code=403, detail="Only doctors can view this")

    doctor = doctor_service.get_doctor_profile(db, current_user)
    return appointment_service.get_appointments_by_doctor(db, doctor.id)

@router.put("/{appointment_id}/status", response_model=schemas.AppointmentResponse)
def update_status(
    appointment_id: int,
    update: schemas.AppointmentUpdate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    if current_user.role != "DOCTOR":
        raise HTTPException(status_code=403, detail="Only doctors can update status")

    appointment = appointment_service.update_appointment_status(db, appointment_id, update.status)
    return appointment
