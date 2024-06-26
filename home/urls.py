# home/urls.py

from django.urls import path
from .views import register, login, add_patient, get_patient, add_heart_rate, get_heart_rate

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('patients/', add_patient, name='add_patient'),
    path('patients/<int:patient_id>/', get_patient, name='get_patient'),
    path('heart_rates/', add_heart_rate, name='add_heart_rate'),
    path('heart_rates/<int:patient_id>/', get_heart_rate, name='get_heart_rate'),
]
