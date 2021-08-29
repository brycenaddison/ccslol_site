from django.urls import path

from . import views

app_name = 'page_playoffs'
urlpatterns = [
    path('', views.root, name='root'),
]
