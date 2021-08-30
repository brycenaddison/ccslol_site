from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.utils import timezone

from backend_database.models import Article

# Create your views here.

def root(request):
    return render(request, 'page_blog_html/main.html')


def write(request):
    if request.user.is_authenticated:
        return render(request, 'page_blog_html/write.html')
    messages.add_message(request, messages.WARNING, 'You must be signed in to do that!')
    return redirect(reverse("page_home:root"))


def view_article(request, article_id):
    article = Article.objects.filter(id=article_id)
    
    context = {
        "article": article[0],
        "article_date_converted": convert_to_localtime(article[0].date_posted)
    }
    return render(request, 'page_blog_html/article.html', context)

import pytz

def convert_to_localtime(utctime):
    utc = utctime.replace(tzinfo=pytz.UTC)
    return utc.astimezone(timezone.get_current_timezone())