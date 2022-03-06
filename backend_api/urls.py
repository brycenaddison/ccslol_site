from django.urls import path

from . import views

app_name = 'backend_api'
urlpatterns = [
    path('blog/post', views.blog_post, name='blog_post'),
    path('blog/edit', views.blog_edit, name='blog_edit'),
]
