from django.urls import path

from . import views

app_name = 'page_twitch'
urlpatterns = [
    path('', views.root, name='root'),
]
