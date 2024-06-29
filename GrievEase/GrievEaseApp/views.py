from django.shortcuts import render
from models import CustomUser, Grievance_Data
from django.contrib import admin
# Create your views here.
admin.site.register(CustomUser)
admin.site.register(Grievance_Data)
admin.site.site_header = 'GrievEase Admin'
admin.site.site_title = 'GrievEase Admin Portal'
admin.site.index_title = 'Welcome to GrievEase Admin Portal'