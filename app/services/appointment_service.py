from app import models, schemas

def book_appointment(db, patient, data: schemas.AppointmentCreate):
    appointment = models.Appointment(
        patient_id=patient.id,
        doctor_id=data.doctor_id,
        appointment_date=data.appointment_date,
        appointment_time=data.appointment_time,
        reason=data.reason
    )
    db.add(appointment)
    db.commit()
    db.refresh(appointment)
    return appointment

def get_appointments_by_patient(db, patient_id: int):
    return db.query(models.Appointment).filter_by(patient_id=patient_id).all()

def get_appointments_by_doctor(db, doctor_id: int):
    return db.query(models.Appointment).filter_by(doctor_id=doctor_id).all()

def update_appointment_status(db, appointment_id: int, status: str):
    appointment = db.query(models.Appointment).filter_by(id=appointment_id).first()
    if not appointment:
        raise Exception("Appointment not found")
    appointment.status = status
    db.commit()
    db.refresh(appointment)
    return appointment
