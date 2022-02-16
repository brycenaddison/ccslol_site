from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_http_methods, require_GET

# Create your views here.

@require_GET
def root(request):
    if request.user.is_authenticated:
        return render(request, 'auth_staff_html/main.html')
    
    messages.add_message(request, messages.WARNING, 'You must be signed in to do that!')
    return redirect(reverse("page_home:root"))


@require_http_methods(["GET", "POST"])
def staff_login(request):
    if not request.user.is_authenticated:
        # Allow unauthenticated to log in.
        if request.method == "GET":
            return render(request, 'auth_staff_html/login.html')

        # Check the unauthenticated user's credentials
        elif request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)

            # Success!
            if user is not None:
                login(request, user)
                return redirect(reverse('page_home:root'))
            
            # Invalid :(
            else:
                messages.add_message(request, messages.WARNING, "Login Failed!")
                return render(request, 'auth_staff_html/login.html')
    
    # Why are you logging in when already signed in?
    messages.add_message(request, messages.WARNING, "You are already signed in!")
    return redirect(reverse('page_home:root'))


@require_GET
def staff_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect(reverse('page_home:root'))


@require_http_methods(["GET", "POST"])
def staff_password(request):
    if request.user.is_authenticated:
        # Allow the user to change their password
        if request.method == 'GET':
            form = PasswordChangeForm(request.user)
            return render(request, 'auth_staff_html/password.html', {'form': form})

        # Validate their credentials before changing password
        elif request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)

            # Success!
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.add_message(request, messages.SUCCESS, "Password successfully updated!")
                return redirect(reverse('page_home:root'))

            # Invalid :(
            else:
                messages.add_message(request, messages.ERROR, 'Please correct the error below.')
                return render(request, 'auth_staff_html/password.html', {'form': form})

    # User tries to access options without being signed in?
    messages.add_message(request, messages.WARNING, 'You must be signed in to do that!')
    return redirect(reverse("page_home:root"))