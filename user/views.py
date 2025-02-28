from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


########### register here ##################################### 
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # This automatically triggers the signal to send the email

            messages.success(request, 'Your account has been created! You are now able to log in.')
            return redirect('login')  # Ensure 'login' matches the name in your urls.py

    else:
        form = UserRegisterForm()
    
    return render(request, 'user/register.html', {'form': form, 'title': 'Register Here'})


################ login form ################################################### 
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Corrected usage
            messages.success(request, f'Welcome {username}!')
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password. Please try again.')

    form = AuthenticationForm()
    return render(request, 'user/login.html', {'form': form, 'title': 'Log In'})

def logout_view(request):
    logout(request)
    return redirect('index') 