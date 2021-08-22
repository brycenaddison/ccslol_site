from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'page_news_html/main.html')