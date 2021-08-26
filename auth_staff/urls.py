from django.urls import path

from . import views

app_name = 'auth_staff'
urlpatterns = [
    path('', views.root, name='root'),
    path('login', views.staff_login, name='login'),
    path('logout', views.staff_logout, name='logout'),
    path('options', views.staff_options, name='options'), # Allow user change password here
]
