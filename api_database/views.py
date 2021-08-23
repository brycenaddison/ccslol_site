from django.contrib import messages
from django.http import JsonResponse, HttpResponseForbidden, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.http import require_POST

from api_database.models import Article

# Create your views here.

@require_POST
def news_post(request):
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