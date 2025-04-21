from sqlalchemy import Column, String, Integer, ForeignKey, Text, DateTime, Time, Date
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base
from sqlalchemy import Boolean

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(String, nullable=False)  # "PATIENT" or "DOCTOR" or "ADMIN"
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    doctor_profile = relationship("Doctor", uselist=False, back_populates="user")
    patient_profile = relationship("Patient", uselist=False, back_populates="user")

class Doctor(Base):
    __tablename__ = "doctor_profiles"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    specialization = Column(String, nullable=False)
    city = Column(String, nullable=False)
    bio = Column(Text)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    is_active = Column(Boolean, default=True)

    user = relationship("User", back_populates="doctor_profile")
    availability = relationship("Availability", back_populates="doctor")
    appointments = relationship("Appointment", back_populates="doctor")

class Patient(Base):
    __tablename__ = "patients"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    age = Column(Integer, nullable=False)
    gender = Column(String, nullable=False)
    city = Column(String, nullable=False)
    contact_number = Column(String)

    user = relationship("User", back_populates="patient_profile")
    appointments = relationship("Appointment", back_populates="patient")

class Availability(Base):
    __tablename__ = "availability"
    
    id = Column(Integer, primary_key=True)
    doctor_id = Column(Integer, ForeignKey("doctor_profiles.id"))
    day_of_week = Column(String, nullable=False)
    start_time = Column(Time, nullable=False)
    end_time = Column(Time, nullable=False)

    doctor = relationship("Doctor", back_populates="availability")

class Appointment(Base):
    __tablename__ = "appointments"
    
    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    doctor_id = Column(Integer, ForeignKey("doctor_profiles.id"))  # Corrected table name
    appointment_date = Column(Date, nullable=False)
    appointment_time = Column(Time, nullable=False)
    status = Column(String, default="PENDING")  # PENDING, CONFIRMED, REJECTED, COMPLETED
    reason = Column(String)

    patient = relationship("Patient", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")
