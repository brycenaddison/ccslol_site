from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def root(request):
    return render(request, 'page_home_html/main.html')


def riot_txt(request):
    return HttpResponse('df06b387-40e3-4a1a-a2db-1759c90669d9')