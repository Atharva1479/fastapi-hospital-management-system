from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, database
from app.services import search_service
from typing import List

router = APIRouter(prefix="/search", tags=["Search"])

@router.get("/doctors", response_model=List[schemas.DoctorSearchResponse])
def search_doctors(city: str = None, specialization: str = None, db: Session = Depends(database.get_db)):
    doctors = search_service.search_doctors(db, city, specialization)
    return [
        schemas.DoctorSearchResponse(
            full_name=doctor.user.full_name,
            email=doctor.user.email,
            specialization=doctor.specialization,
            city=doctor.city,
            bio=doctor.bio
        )
        for doctor in doctors
    ]
