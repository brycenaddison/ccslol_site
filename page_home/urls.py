from django.urls import path

from . import views

app_name = 'page_home'
urlpatterns = [
    path('', views.root, name='root'),
    path('riot.txt', views.riot_txt, name='riot_txt')
]
