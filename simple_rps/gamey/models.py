from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class MatchResult(models.Model):
    user_move = models.CharField(max_length=50)
    npc_move = models.CharField(max_length=50)
    player1_move = models.CharField(max_length=50)
    player2_move = models.CharField(max_length=50)
    winner = models.CharField(max_length=50)

# Create your models here.
