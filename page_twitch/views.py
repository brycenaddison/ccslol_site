from django.shortcuts import render

# Create your views here.

def root(request):
    return render(request, 'page_twitch_html/main.html')
