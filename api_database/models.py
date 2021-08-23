from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Article(models.Model):

    author = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=256)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    last_edited = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title + ', by ' + self.author.username + ', last edited ' + str(self.last_edited)
