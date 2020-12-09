from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        blank=True,
        default='',
    )
    github = models.URLField(blank=True, default='')
    address = models.TextField(blank=True, default='')
    # date_of_birth = models.DateField(blank=True, default=datetime.now)
    personal_website = models.URLField(blank=True, default='')
    about = models.TextField(blank=True, default='')
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.user.username
