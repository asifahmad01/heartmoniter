# home/views.py

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer, PatientSerializer, HeartRateSerializer
from .models import session, User, Patient, HeartRate
from sqlalchemy.exc import IntegrityError

@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        new_user = User(email=email, password=password)
        try:
            session.add(new_user)
            session.commit()
            return Response({'status': 'User registered successfully'})
        except IntegrityError:
            session.rollback()
            return Response({'error': 'User with this email already exists'}, status=400)
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    user = session.query(User).filter_by(email=email, password=password).first()
    if user:
        return Response({'status': 'Login successful'})
    return Response({'error': 'Invalid credentials'}, status=400)

@api_view(['POST'])
def add_patient(request):
    serializer = PatientSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        age = serializer.validated_data['age']
        user_id = serializer.validated_data['user_id']
        new_patient = Patient(name=name, age=age, user_id=user_id)
        session.add(new_patient)
        session.commit()
        return Response({'status': 'Patient added successfully'})
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_patient(request, patient_id):
    patient = session.query(Patient).filter_by(id=patient_id).first()
    if patient:
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    return Response({'error': 'Patient not found'}, status=404)

@api_view(['POST'])
def add_heart_rate(request):
    serializer = HeartRateSerializer(data=request.data)
    if serializer.is_valid():
        patient_id = serializer.validated_data['patient_id']
        heart_rate = serializer.validated_data['heart_rate']
        timestamp = serializer.validated_data['timestamp']
        new_heart_rate = HeartRate(patient_id=patient_id, heart_rate=heart_rate, timestamp=timestamp)
        session.add(new_heart_rate)
        session.commit()
        return Response({'status': 'Heart rate recorded successfully'})
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_heart_rate(request, patient_id):
    heart_rates = session.query(HeartRate).filter_by(patient_id=patient_id).all()
    serializer = HeartRateSerializer(heart_rates, many=True)
    return Response(serializer.data)
