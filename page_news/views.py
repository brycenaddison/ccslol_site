from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

def root(request):
    return render(request, 'page_news_html/main.html')


@login_required
def write(request):
    return render(request, 'page_news_html/write.html')