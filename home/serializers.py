# home/serializers.py

from rest_framework import serializers
from .models import User, Patient, HeartRate

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class PatientSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    user_id = serializers.IntegerField()

class HeartRateSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    patient_id = serializers.IntegerField()
    heart_rate = serializers.IntegerField()
    timestamp = serializers.CharField()
