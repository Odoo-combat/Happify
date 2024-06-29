from django.db import models

# make custom user model for implementin login and registration
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class CustomUser(AbstractUser):
    is_employer = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_grievance_member = models.BooleanField(default=False)
    is_grievance_officer = models.BooleanField(default=False)
    is_grievance_head = models.BooleanField(default=False)
    is_grievance_coordinator = models.BooleanField(default=False)

# Create your models here.
class Grievance_Data(models.Model):
    Description = models.CharField(max_length=1000)
    Evidence = models.ImageField(upload_to='images/')
    Grievance_Type = models.CharField(max_length=100)
    Date_Of_Incident = models.DateField()
    Location = models.CharField(max_length=100)
    resolution = models.CharField(max_length=1000)
    witness_name = models.CharField(max_length=100)
    previos_complaint = models.CharField(max_length=1000)
    comments = models.CharField(max_length=1000)
    status = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    grievance_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    GRIEVANCE_TYPE_CHOICES = [
        ('Harassment', 'Harassment'),
        ('Discrimination', 'Discrimination'),
        ('Workplace Safety', 'Workplace Safety'),
        ('Pay/Benefits', 'Pay/Benefits'),
        ('Other', 'Other'),
    ]

    RESOLUTION_CHOICES = [
        ('Apology', 'Apology'),
        ('Compensation', 'Compensation'),
        ('Policy Change', 'Policy Change'),
        ('Other', 'Other'),
    ]
    def __str__(self):
        return self.Grievance_Type
    