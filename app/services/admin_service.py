from app import models
from sqlalchemy import func

def get_all_doctors(db):
    doctors = db.query(models.Doctor).join(models.User).all()

    response = []
    for doctor in doctors:
        response.append({
            "id": doctor.id,
            "full_name": doctor.user.full_name,
            "email": doctor.user.email,
            "specialization": doctor.specialization,
            "city": doctor.city,
            "is_active": getattr(doctor, "is_active", True)  # add default if missing
        })
    return response

def get_all_patients(db):
    patients = db.query(models.Patient).join(models.User).all()

    response = []
    for patient in patients:
        response.append({
            "id": patient.id,
            "full_name": patient.user.full_name,
            "email": patient.user.email,
            "age": patient.age,
            "city": patient.city,
        })
    return response

def get_all_appointments(db):
    return db.query(models.Appointment).all()

def toggle_doctor_status(db, doctor_id: int):
    doctor = db.query(models.Doctor).filter(models.Doctor.id == doctor_id).first()
    if not doctor:
        raise Exception("Doctor not found")
    doctor.is_active = not doctor.is_active
    db.commit()
    db.refresh(doctor)
    return doctor

def get_system_stats(db):
    return {
        "total_doctors": db.query(models.Doctor).count(),
        "total_patients": db.query(models.Patient).count(),
        "total_appointments": db.query(models.Appointment).count()
    }

def get_appointment_count_per_doctor(db):
    results = db.query(
        models.Doctor.id,
        models.User.full_name,
        func.count(models.Appointment.id)
    ).join(models.Doctor.user
    ).outerjoin(models.Appointment
    ).group_by(models.Doctor.id, models.User.full_name).all()

    return [
        {
            "doctor_id": r[0],
            "doctor_name": r[1],
            "appointment_count": r[2]
        } for r in results
    ]

def get_daily_appointment_trend(db):
    results = db.query(
        func.date(models.Appointment.appointment_date),
        func.count(models.Appointment.id)
    ).group_by(
        func.date(models.Appointment.appointment_date)
    ).order_by(
        func.date(models.Appointment.appointment_date)
    ).all()

    return [{"date": r[0], "count": r[1]} for r in results]

