from app import models, schemas

def create_patient_profile(db, user, patient_data: schemas.PatientCreate):
    if user.role != "PATIENT":
        raise Exception("Only patients can create profiles")

    profile = models.Patient(**patient_data.dict(), user_id=user.id)
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile

def get_patient_profile(db, user):
    return db.query(models.Patient).filter(models.Patient.user_id == user.id).first()
