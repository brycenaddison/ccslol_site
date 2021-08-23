from django.urls import path

from . import views

app_name = 'api_database'
urlpatterns = [
    path('news/post', views.news_post, name='news_post'),
]
