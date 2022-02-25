from django.http import HttpResponse
from django.shortcuts import render

from backend_database.models import Article

# Create your views here.

def root(request):
    most_recent_article = None
    if Article.objects.exists():
        most_recent_article = Article.objects.latest("date_posted")
    
    context = {
        "most_recent_article": most_recent_article
    }
    return render(request, 'page_home_html/main.html', context)


def riot_txt(request):
    return HttpResponse('d287159e-e412-4645-b764-1db4d94eb852')