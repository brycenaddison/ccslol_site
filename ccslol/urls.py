"""ccslol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    path('', include('page_home.urls')),
    path('about/', include('page_about.urls')),
    path('blog/', include('page_blog.urls')),
    path('playoffs/', include('page_playoffs.urls')),
    path('schedule/', include('page_schedule.urls')),
    path('standings/', include('page_standings.urls')),
    path('twitch/', include('page_twitch.urls')),
    # Non user-facing
    path('api/', include('backend_api.urls')),
    path('admin/', admin.site.urls),
    path('staff/', include('auth_staff.urls')),
    # Timezone detection (django-tz-detect)
    re_path(r'^tz_detect/', include('tz_detect.urls'))
]
