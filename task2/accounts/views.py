from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import PatientSignUpForm, DoctorSignUpForm, PatientLoginForm, DoctorLoginForm
from .models import User

class PatientSignUpView(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:patient_dashboard')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'patient'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('accounts:patient_dashboard')

class DoctorSignUpView(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:doctor_dashboard')

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'doctor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('accounts:doctor_dashboard')

class PatientLoginView(LoginView):
    form_class = PatientLoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('accounts:patient_dashboard')

    def get_success_url(self):
        return reverse_lazy('accounts:patient_dashboard')

class DoctorLoginView(LoginView):
    form_class = DoctorLoginForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('accounts:doctor_dashboard')

    def get_success_url(self):
        return reverse_lazy('accounts:doctor_dashboard')

class PatientDashboardView(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'accounts/patient_dashboard.html'
    fields = ['first_name', 'last_name', 'email', 'address_line1', 'city', 'state', 'pincode', 'profile_picture']

    def get_success_url(self):
        return reverse_lazy('accounts:patient_dashboard')

    def get_object(self):
        return self.request.user

class DoctorDashboardView(LoginRequiredMixin, CreateView):
    model = User
    template_name = 'accounts/doctor_dashboard.html'
    fields = ['first_name', 'last_name', 'email', 'address_line1', 'city', 'state', 'pincode', 'profile_picture']

    def get_success_url(self):
        return reverse_lazy('accounts:doctor_dashboard')

    def get_object(self):
        return self.request.user

class LogoutView(LogoutView):
    template_name = 'accounts/logout.html'
