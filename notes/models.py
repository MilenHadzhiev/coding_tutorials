from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
