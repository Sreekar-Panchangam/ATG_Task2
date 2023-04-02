from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate
from .models import User

class PatientSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    address_line1 = forms.CharField(max_length=255, required=True)
    city = forms.CharField(max_length=255, required=True)
    state = forms.CharField(max_length=255, required=True)
    pincode = forms.CharField(max_length=255, required=True)
    profile_picture = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'address_line1', 'city', 'state', 'pincode', 'profile_picture')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_patient = True
        user.save()
        return user

class DoctorSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, required=True)
    address_line1 = forms.CharField(max_length=255, required=True)
    city = forms.CharField(max_length=255, required=True)
    state = forms.CharField(max_length=255, required=True)
    pincode = forms.CharField(max_length=255, required=True)
    profile_picture = forms.ImageField(required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'address_line1', 'city', 'state', 'pincode', 'profile_picture')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_doctor = True
        user.save()
        return user

class PatientLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Invalid login credentials. Please try again.")
            elif not user.is_patient:
                raise forms.ValidationError("You do not have access to the patient dashboard.")
        return cleaned_data

class DoctorLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("Invalid login credentials. Please try again.")
            elif not user.is_doctor:
                raise forms.ValidationError("You do not have access to the doctor dashboard.")
        return cleaned_data
