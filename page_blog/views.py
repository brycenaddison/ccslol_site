from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.utils import timezone

from backend_database.models import Article

# Create your views here.

def root(request):
    try:
        count = int(request.GET.get('page', '1'))
    except:
        count = 1
    if count < 1:
        count = 1

    per_page = 10
    page_count = (Article.objects.count() // per_page) + 1
    page_range = range(1, page_count + 1)

    if count not in page_range:
        return redirect('{}?page=1'.format(reverse("page_blog:root")))

    articles = Article.objects.order_by("-date_posted")[per_page * (count - 1):per_page * count]

    context = {
        "articles": articles,
        "page_range": page_range,
        "page_current": count,
        "page_max": (Article.objects.count() // per_page) + 1,
    }

    return render(request, 'page_blog_html/main.html', context)


def write_article(request):
    if request.user.is_authenticated:
        return render(request, 'page_blog_html/write.html')
    else:
        messages.add_message(request, messages.WARNING, 'You must be signed in to do that!')
    return redirect(reverse("page_blog:root"))


def edit_article(request, article_id):
    if request.user.is_authenticated:
        article_query = Article.objects.filter(id=article_id)

        if article_query.exists():
            context = {
                "article": article_query[0]
            }

            return render(request, 'page_blog_html/edit.html', context)
    else:
        messages.add_message(request, messages.WARNING, 'You must be signed in to do that!')

    return redirect(reverse("page_blog:root"))


def view_article(request, article_id):
    article_query = Article.objects.filter(id=article_id)
    
    if article_query.exists():
        context = {
            "article": article_query[0]
        }
        
        return render(request, 'page_blog_html/article.html', context)
    
    return redirect(reverse("page_blog:root"))


# Timezones
import pytz

def convert_to_localtime(utctime):
    utc = utctime.replace(tzinfo=pytz.UTC)
    return utc.astimezone(timezone.get_current_timezone())