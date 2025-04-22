from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from Contact.models import User_Contact
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'index.html')    # You can access request.user in the template

def about(request):
    return render(request,'about.html')

def contact(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            User_Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            success = True

    return render(request, 'contact.html', {'success': success})


def courses(request):
    return render(request,'courses.html')

def instructor(request):
    return render(request,'instructor.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)

            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Logged in successfully.')
                return redirect('home')  # change 'home' to your dashboard or landing page
            else:
                messages.error(request, 'Invalid credentials.')

        except User.DoesNotExist:
            messages.error(request, 'No account found with this email.')

    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Account created successfully.')
            return redirect('login')
            
    return render(request, 'signup.html')

def single(request):
    return render(request,'single.html')

def team(request):
    return render(request,'team.html')

def testimonial(request):
    return render(request,'testimonial.html')

def logout(request):
    auth_logout(request)
    return redirect('login')  # or redirect('home') if you prefer