# forms.py

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import JobApplication, Employee,JobPosting, HR
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Employee,HR

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email','first_name', 'password1', 'password2']

class CompanyRegistrationForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields=['mobile','profile_photo','description','location','website']

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = HR
        fields = ['cgpa', 'resume', 'enrollment_no', 'branch', 'semester', 'batch', 'roll_no']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        db_table = ''
        managed = True
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        fields = ["email",'first_name']

class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = HR
        fields = ['cgpa', 'resume', 'enrollment_no', 'branch', 'semester', 'batch', 'roll_no']

class CompanyUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['mobile','profile_photo','description','location','website']