from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    user_id = models.PositiveBigIntegerField()
    followers = models.PositiveSmallIntegerField()
    following = models.PositiveSmallIntegerField()
    friends = models.PositiveSmallIntegerField()
    avatar_url = models.URLField()

