from django.shortcuts import render

# Create your views here.

def root(request):
    return render(request, 'page_schedule_html/main.html')