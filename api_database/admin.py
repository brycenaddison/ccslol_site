from django.contrib import admin

# Register your models here.

from .models import *

class ArticleAdmin(admin.ModelAdmin):
    pass

admin.site.register(Article, ArticleAdmin)
