from django.shortcuts import render

# Create your views here.

def root(request):
    return render(request, 'auth_staff_html/main.html')