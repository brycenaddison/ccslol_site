from django.urls import path

from . import views

app_name = 'page_news'
urlpatterns = [
    path('', views.homepage, name='homepage'),
]
