from fastapi import APIRouter, Depends, HTTPException
from app import models, schemas, database, auth
from app.services import patient_service
from sqlalchemy.orm import Session

router = APIRouter(prefix="/patient", tags=["Patient"])

@router.post("/profile", response_model=schemas.PatientResponse)
def create_profile(
    patient_data: schemas.PatientCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    try:
        profile = patient_service.create_patient_profile(db, current_user, patient_data)
        return schemas.PatientResponse(
            id=profile.id,
            full_name=current_user.full_name,
            email=current_user.email,
            age=profile.age,
            gender=profile.gender,
            city=profile.city,
            contact_number=profile.contact_number
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/profile", response_model=schemas.PatientResponse)
def get_profile(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    profile = patient_service.get_patient_profile(db, current_user)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return schemas.PatientResponse(
        id=profile.id,
        full_name=current_user.full_name,
        email=current_user.email,
        age=profile.age,
        gender=profile.gender,
        city=profile.city,
        contact_number=profile.contact_number
    )
