from django.shortcuts import render

# Create your views here.

def root(request):
    return render(request, 'page_about_html/main.html')