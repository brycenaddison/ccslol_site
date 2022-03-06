from django.contrib import messages
from django.http import JsonResponse, HttpResponseForbidden, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.http import require_POST

from backend_database.models import Article

# Create your views here.

@require_POST
def blog_post(request):
    if request.is_ajax() and request.user.is_authenticated:
        article_title = request.POST.get('article_title')
        article_content = request.POST.get('article_content')

        if not article_title or not article_content:
            return HttpResponseBadRequest()

        obj = Article.objects.create(author=request.user,
                                    title=article_title,
                                    content=article_content)
        obj.save()

        messages.add_message(request, messages.SUCCESS, "Article created!")
        return JsonResponse({})

    return HttpResponseForbidden()


@require_POST
def blog_edit(request):
    if request.is_ajax() and request.user.is_authenticated:
        article_id = request.POST.get('article_id')
        article_title = request.POST.get('article_title')
        article_content = request.POST.get('article_content')

        if not article_id or not article_title or not article_content:
            return HttpResponseBadRequest()

        article_query = Article.objects.filter(id=article_id)
        
        if article_query.exists():
            article = article_query[0]
            article.title = article_title
            article.content = article_content
            article.last_edited_by = request.user
            article.save()

            messages.add_message(request, messages.SUCCESS, "Article edited!")
            return JsonResponse({})
        
        else:
            messages.add_message(request, messages.ERROR, "Article does not exist at that ID!")
            return HttpResponseBadRequest()

    return HttpResponseForbidden()