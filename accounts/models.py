from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    profile_picture = models.ImageField(
        upload_to='profile_pics/'
    )
    github = models.URLField()
    address = models.TextField()
    date_of_birth = models.DateField()
    personal_website = models.URLField()
    about = models.TextField()
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.user.username
