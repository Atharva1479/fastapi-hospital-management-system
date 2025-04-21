from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date, time

class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    role: str  # "PATIENT" or "DOCTOR" or "ADMIN"

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class DoctorCreate(BaseModel):
    specialization: str
    bio: Optional[str]
    city: str

class PatientCreate(BaseModel):
    age: int
    gender: str
    city: str
    contact_number: Optional[str]

class PatientResponse(BaseModel):
    id: int
    full_name: str
    email: str
    age: int
    gender: str
    city: str
    contact_number: Optional[str]

    class Config:
        orm_mode = True

class DoctorSearchResponse(BaseModel):
    full_name: str
    email: str
    specialization: str
    city: str
    bio: Optional[str]

    class Config:
        orm_mode = True

class DoctorResponse(BaseModel):
    id: int
    full_name: str
    email: str
    specialization: str
    bio: Optional[str]
    city: str

    class Config:
        orm_mode = True

class AppointmentCreate(BaseModel):
    doctor_id: int
    appointment_date: date
    appointment_time: time
    reason: Optional[str]

class AppointmentResponse(BaseModel):
    id: int
    doctor_id: int
    patient_id: int
    appointment_date: date
    appointment_time: time
    status: str
    reason: Optional[str]

    class Config:
        orm_mode = True

class AppointmentUpdate(BaseModel):
    status: str  # e.g., CONFIRMED, REJECTED

class AdminDoctorResponse(BaseModel):
    id: int
    full_name: str
    email: str
    specialization: str
    city: str
    is_active: bool

    class Config:
        orm_mode = True

class AdminPatientResponse(BaseModel):
    id: int
    full_name: str
    email: str
    age: int
    city: str

    class Config:
        orm_mode = True

class AdminAppointmentResponse(BaseModel):
    id: int
    patient_id: int
    doctor_id: int
    appointment_date: date
    appointment_time: time
    status: str
    reason: Optional[str]

    class Config:
        orm_mode = True

class SystemStats(BaseModel):
    total_doctors: int
    total_patients: int
    total_appointments: int

class AppointmentCountPerDoctor(BaseModel):
    doctor_id: int
    doctor_name: str
    appointment_count: int

class DailyAppointmentTrend(BaseModel):
    date: date
    count: int

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    user_id: Optional[int] = None
