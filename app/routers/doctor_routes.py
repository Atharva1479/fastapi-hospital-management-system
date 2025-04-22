from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, models, database, auth
from app.services import doctor_service

router = APIRouter(prefix="/doctor", tags=["Doctor"])

@router.post("/profile", response_model=schemas.DoctorResponse)
def create_profile(
    doctor_data: schemas.DoctorCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    try:
        profile = doctor_service.create_doctor_profile(db, current_user, doctor_data)
        return schemas.DoctorResponse(
            id=profile.id,
            full_name=current_user.full_name,
            email=current_user.email,
            specialization=profile.specialization,
            bio=profile.bio,
            city=profile.city
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/profile", response_model=schemas.DoctorResponse)
def get_profile(
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    profile = doctor_service.get_doctor_profile(db, current_user)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    
    return schemas.DoctorResponse(
        id=profile.id,
        full_name=current_user.full_name,
        email=current_user.email,
        specialization=profile.specialization,
        bio=profile.bio,
        city=profile.city
    )

@router.put("/profile", response_model=schemas.DoctorResponse)
def update_profile(
    doctor_data: schemas.DoctorCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(auth.get_current_user)
):
    try:
        profile = doctor_service.update_doctor_profile(db, current_user, doctor_data)
        return schemas.DoctorResponse(
            id=profile.id,
            full_name=current_user.full_name,
            email=current_user.email,
            specialization=profile.specialization,
            bio=profile.bio,
            city=profile.city
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e)) 
   
