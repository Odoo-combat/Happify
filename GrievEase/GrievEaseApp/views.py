from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import \
    login as auth_login  # Rename the login function to avoid conflicts
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .forms import (CompanyRegistrationForm, CompanyUpdateForm, StudentRegistrationForm,
                    StudentUpdateForm,UserRegistrationForm,UserUpdateForm)
from .models import Employee, JobPosting, HR

# Create your views here.
def home(request):
    companies = []
    context = {
        'companies': companies
    }
    return render(request, 'companies.html', context)


def ourstudents(request):
    hr = []
    hr += HR.objects.all()
    context = {
        'hr': hr
    }
    return render(request, 'companies.html', context)

def aboutus(request):
    return render(request,'aboutus.html')

def company_signup(request):
    if request.method == "POST":
        u_form = UserRegistrationForm(request.POST)
        p_form = CompanyRegistrationForm(request.POST)
        if (u_form.is_valid() and p_form.is_valid()):
            u_form.save()
            p_form.save()
            username = u_form.cleaned_data.get("username")
            messages.success(request, f"Your account has been created! You are now able to log in")
            return redirect("login")
    else:
        u_form = UserRegistrationForm()
        p_form = CompanyRegistrationForm()

        context = {
        "u_form": u_form,
        "p_form": p_form
        }

    return render(request,"company_signup.html",context)



def student_signup(request):
    if request.method == 'POST':
        student_registration_form = StudentRegistrationForm(request.POST)
        if student_registration_form.is_valid():
            #save user to user table aswell instead of just employee table
            
            user = student_registration_form.save()
            username = student_registration_form.cleaned_data.get('username')
            raw_password = student_registration_form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            return redirect('user_login')  # Redirect to the user's profile after registration
        else:
            messages.error(request, 'Please correct the error below.')
            return render(request, 'student_signup.html', {'student_registration_form': student_registration_form})
    elif request.method == "GET":
        student_registration_form = StudentRegistrationForm()  # Default to the employee registration form
        return render(request, 'student_signup.html', {'student_registration_form': student_registration_form})

def jobpost_create(request):
    
        return render(request, 'company_signup.html')

def user_login(request):
    if request.method == "POST":
        # Get the submitted login form data
        login_form = AuthenticationForm(data=request.POST)

        if login_form.is_valid():
            # Authentication
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            # Try to authenticate with both Employee and HR models
            company_user = authenticate(request, username=username, password=password, model=Employee)
            student_user = authenticate(request, username=username, password=password, model=HR)

            # Check if either authentication is successful
            if company_user is not None:
                auth_login(request, company_user)
                return redirect('home')  # Redirect to the home page upon successful login
            elif student_user is not None:
                auth_login(request, student_user)
                return redirect('home')  # Redirect to the home page upon successful login
            else:
                # Authentication failed for both types, show an error message
                login_form.add_error(None, 'Invalid username or password.')

    else:
        # Handle GET request for the login form

        if request.user.is_authenticated:
            return redirect('home')  # Redirect authenticated users to the home page
        else:
            login_form = AuthenticationForm()

    # Render the login form template with the login_form context variable
    return render(request, 'user_login.html', {'login_form': login_form})

def company_update(request):
   
    return render(request, 'company_update.html', )

def student_update(request):
    
    return render(request, 'student_update.html', )

def jobpost_update(request):
    
    return render(request, 'jobpost_update.html', )
def company_profile(request):
    pass
def student_profile(request):
    pass
def jobpost(request):
    return render(request, 'jobpost_create.html', )



def user_logout(request):
    """Logs out a logged in user."""
    logout(request)
    return redirect('user_login')

def temp(request):
    if request.method == 'POST':
        return redirect('user_login')
    elif request.method == 'GET' :
        return render(request, 'company_signup.html' )
    

    
