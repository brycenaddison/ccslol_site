from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Article(models.Model):
    
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name="post_author")
    title = models.CharField(max_length=256)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    last_edited = models.DateTimeField(auto_now=True)
    last_edited_by = models.ForeignKey(User, on_delete = models.CASCADE, null=True, related_name="edit_author")
    
    def __str__(self):
        return self.title + ', by ' + self.author.username + ', last edited ' + str(self.last_edited) + ' by ' + self.last_edited_by


class Season(models.Model):

    name = models.CharField(max_length=64, unique=True)
    date_created = models.DateTimeField(default=timezone.now)


class Role(models.Model):

    name = models.CharField(max_length=16, unique=True)


class Team(models.Model):

    name = models.CharField(max_length=64)
    season = models.ForeignKey(Season, null=True, on_delete=models.SET_NULL)
    game_wins = models.IntegerField(default=0)
    game_losses = models.IntegerField(default=0)
    match_wins = models.IntegerField(default=0)
    match_losses = models.IntegerField(default=0)
    date_created = models.DateTimeField(default=timezone.now)


class Player(models.Model):

    name = models.CharField(max_length=64)
    season = models.ForeignKey(Season, null=True, on_delete=models.SET_NULL)
    team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)
    role = models.ForeignKey(Role, null=True, on_delete=models.SET_NULL)
    is_sub = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=timezone.now)


class Match(models.Model):

    season = models.ForeignKey(Season, null=True, on_delete=models.SET_NULL)
    winner = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL, related_name="match_winner")
    loser = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL, related_name="match_loser")
    winner_score = models.IntegerField(default=0)
    loser_score = models.IntegerField(default=0)


class Game(models.Model):

    season = models.ForeignKey(Season, null=True, on_delete=models.SET_NULL)
    match = models.ForeignKey(Match, null=True, on_delete=models.SET_NULL)
    winner = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL, related_name="game_winner")
    loser = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL, related_name="game_loser")
