from django.db import models
from django.contrib.auth.models import  Group, Permission, User
from django.core.validators import (FileExtensionValidator, MaxValueValidator,
                                    MinValueValidator, RegexValidator)
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image


# Create your models here.
class Employee(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    mobile = PhoneNumberField(blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos', blank=True)
    description = models.TextField(blank=True)
    verification = models.BooleanField(default=False)

    location = models.CharField(max_length=100, blank=True)
    website = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self,*args,**kwargs):
        super(Employee,self).save(*args,**kwargs)
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)


# Custom User Model for HR
class HR(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    mobile = PhoneNumberField(blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos', blank=True)
    description = models.TextField(blank=True)
    verification = models.BooleanField(default=False)

    cgpa = models.DecimalField(max_digits=4, decimal_places=2, validators=[
        MinValueValidator(0), MaxValueValidator(10)])
    resume = models.FileField(upload_to='resumes/', blank=True)
    enrollment_no = models.PositiveIntegerField(validators=[MaxValueValidator(999999999999)])
    branch = models.CharField(max_length=50, blank=True)
    semester = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(8)], default=1)
    batch = models.CharField(max_length=3)
    roll_no = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(999)])
    # date_of_birth = models.DateField()
    applied_postings = models.ManyToManyField('JobPosting', blank=True)

    EMPLOYED = 'Employed'
    UNEMPLOYED = 'Unemployed'
    JOB_STATUS_CHOICES = [
        (EMPLOYED, 'Employed'),
        (UNEMPLOYED, 'Unemployed'),
    ]
    job_status = models.CharField(
        max_length=10,
        choices=JOB_STATUS_CHOICES,
        default=UNEMPLOYED,
    )
    job_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self,*args,**kwargs):
        super(HR,self).save(*args,**kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

# Job Posting Model
class JobPosting(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    job_description = models.TextField()
    salary = models.PositiveIntegerField()
    deadline_to_apply = models.DateTimeField()
    bond_period = models.CharField(max_length=20)
    duration_of_job = models.CharField(max_length=20)

    def __str__(self):
        return self.title
# Model for Internship Application
class JobApplication(models.Model):
    hr = models.ForeignKey(HR, on_delete=models.CASCADE)
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.hr.user.username} - {self.job_posting.title}"

        
