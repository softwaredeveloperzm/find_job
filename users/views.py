from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User
from .form import RegisterUserForm
from resume.models import Resume
from company.models import Company
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

def register_applicant(request):
    User = get_user_model()  # Get the user model

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']  # Get password from form
            user = User.objects.create_user(username=email, email=email, password=password)
            user.is_applicant = True
            user.save()
            Resume.objects.create(user=user)
            messages.success(request, 'Your account has been created. You can now login.')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
    else:
        form = RegisterUserForm()
    context = {'form': form}
    return render(request, 'users/register_applicant.html', context)






#regiter recruiter only
def register_recruiter(request):
    User = get_user_model() 
    
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']  
            user = User.objects.create_user(username=email, email=email, password=password)
            user.is_applicant = False
            user.is_recruiter = True
            user.save()
            Resume.objects.create(user=user)
            messages.success(request, 'Your account has been created. You can now login.')
            return redirect('login')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error in {field}: {error}")
            return redirect('register_recruiter')
    else:
        form = RegisterUserForm()
        context = {'form': form}
        return render(request, 'users/register_recruiter.html', context)


#login a user
def login_user(request):
    if request.method == 'POST' :
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('dashboard')
            
        else:
            messages.warning(request, 'Incorrect email or password. Please try again.')
            return redirect('login')

    else:
        return render(request, 'users/login.html')
    

def logout_user(request):
    logout(request)
    messages.info(request, 'Your session has ended')
    return redirect('home')

