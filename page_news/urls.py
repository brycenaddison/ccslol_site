from django.urls import path

from . import views

app_name = 'page_news'
urlpatterns = [
    path('', views.root, name='root'),
    path('write', views.write, name='write'),
]
