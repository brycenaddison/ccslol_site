from django.urls import path

from . import views

app_name = 'auth_staff'
urlpatterns = [
    path('', views.root, name='root'),
]
