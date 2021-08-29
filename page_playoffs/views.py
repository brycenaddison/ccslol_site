from django.shortcuts import render

# Create your views here.

def root(request):
    return render(request, 'page_playoffs_html/main.html')
