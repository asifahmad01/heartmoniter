# home/models.py

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

# Define User model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

# Define Patient model
class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='patients')

User.patients = relationship('Patient', order_by=Patient.id, back_populates='user')

# Define HeartRate model
class HeartRate(Base):
    __tablename__ = 'heart_rates'
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    heart_rate = Column(Integer, nullable=False)
    timestamp = Column(String, nullable=False)
    patient = relationship('Patient', back_populates='heart_rates')

Patient.heart_rates = relationship('HeartRate', order_by=HeartRate.id, back_populates='patient')

# Create engine and session
engine = create_engine('sqlite:///db.sqlite3')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
