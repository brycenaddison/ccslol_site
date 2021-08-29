from django.urls import path

from . import views

app_name = 'api_database'
urlpatterns = [
    path('blog/post', views.blog_post, name='blog_post'),
]
