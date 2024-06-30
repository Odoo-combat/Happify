from django.urls import path
from . import views


urlpatterns = [
    #home /companies.html
    path('', views.home, name='home'),
    
    # hr
    path('ourstudents/',views.ourstudents,name='ourstudents'),
    #creators/us
    path('aboutus/',views.aboutus,name="aboutus"),
    
    #sign ups and post creation
    path('company_signup/',views.company_signup,name="company_signup"),
    path('student_signup/',views.student_signup,name="student_signup"),
    path('jobposting/',views.jobpost,name="jobpost_create"),
    
    #login
    path('user_login/',views.user_login,name="user_login"),

    #update data
    path('update_company/',views.company_update,name="company_update"),
    path('update_student/',views.student_update,name="student_update"),
    path('update_jobposting/',views.jobpost_update,name="jobpost_update"),

    path('company_profile/',views.company_profile,name="company_profile"),
    path('student_profile/',views.student_profile,name="student_profile"),
    path('jobposting_profile/',views.jobpost,name="jobpost"),

    #logout
    path('user_logout/',views.user_logout,name="user_logout"),
    
    # temp html page to experiment html pages
    path('temp/',views.temp,name="temp"),
]

