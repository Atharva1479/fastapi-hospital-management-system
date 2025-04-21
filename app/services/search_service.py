from app import models, schemas

def search_doctors(db, city: str = None, specialization: str = None):
    query = db.query(models.Doctor).join(models.User)

    if city:
        query = query.filter(models.Doctor.city.ilike(f"%{city}%"))
    if specialization:
        query = query.filter(models.Doctor.specialization.ilike(f"%{specialization}%"))

    return query.all()
