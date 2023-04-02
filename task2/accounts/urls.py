from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('patientlogin/', views.PatientLoginView.as_view(),name='loginpatient'),
    path('doctorlogin/', views.DoctorLoginView.as_view(),name='logindoctor'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('patientsignup/', views.PatientSignUpView.as_view(), name='signuppatient'),
    path('doctorsignup/', views.DoctorSignUpView.as_view(), name='signupdoctor'),
    path('patientdashboard/', views.PatientDashboardView.as_view(), name='patient_dashboard'),
    path('doctordashboard/', views.DoctorDashboardView.as_view(), name='doctor_dashboard'),
]
