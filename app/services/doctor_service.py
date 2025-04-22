from app import models, schemas

def create_doctor_profile(db, user, doctor_data: schemas.DoctorCreate):
    if user.role != "DOCTOR":
        raise Exception("Only doctors can create profiles")
    
    profile = models.Doctor(**doctor_data.dict(), user_id=user.id)
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile

def get_doctor_profile(db, user):
    return db.query(models.Doctor).filter(models.Doctor.user_id == user.id).first()

def update_doctor_profile(db, user, doctor_data: schemas.DoctorCreate):
    if user.role != "DOCTOR":
        raise Exception("Only doctors can update profiles")
    
    profile = db.query(models.Doctor).filter(models.Doctor.user_id == user.id).first()
    if not profile:
        raise Exception("Profile not found")
    
    for key, value in doctor_data.dict().items():
        setattr(profile, key, value)
    
    db.commit()
    db.refresh(profile)
    return profile
