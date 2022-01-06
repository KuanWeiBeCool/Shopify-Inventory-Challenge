
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm

def register_login(request):
    '''
    View for both sign in and sign up page.
    '''
    form = RegisterForm()
    if request.method == "POST":
        if 'signUp' in request.POST:
            # Register
            form = RegisterForm(request.POST)
            
            if form.is_valid():
                form.save()
                username = request.POST['username']
                password = request.POST['password1']
                user = authenticate(request, username=username, password=password)
                login(request, user)
                messages.success(request, f"Welcome, {username}!")
                return redirect('confirmation')
            # leave sign_up checked so that the page will remain on the sign up page
            return render(request, 'home/login.html', {'form':form, 'sign_up':"checked", 'sign_in':""})
        else:
            # Login
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}!")
                return redirect('home')
            else:
                messages.error(request, "Whoops, your username and password didn't match. Please try again.")
                return render(request, 'home/login.html', {'form':form, 'sign_up':"", 'sign_in':"checked"})
            # leave sign_up checked so that the page will remain on the sign up page

    # When just entered the page, by default will be sign in page
    return render(request, 'home/login.html', {'form':form, 'sign_up':"", 'sign_in':"checked"})


def confirmation(request):
    '''
    View for successfully signed up.
    '''
    return render(request, "home/confirmation.html")

def logout_user(request):
    '''
    View for the logout. 
    '''
    logout(request)
    return redirect('login')