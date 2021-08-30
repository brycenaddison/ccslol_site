from django.urls import path

from . import views

app_name = 'page_blog'
urlpatterns = [
    path('', views.root, name='root'),
    path('write', views.write, name='write'),
    path('article/<int:article_id>', views.view_article, name='view_article'),
]
