from django.contrib.auth.models import User
from django.db import models


class Tutorial(models.Model):
    tutorial_name = models.CharField(
        max_length=35,
    )
    description = models.TextField()
    video_url = models.URLField(blank=True, default='')

    # tutorial_file = models.FileField(
    #     upload_to='tutorial_videos/',
    # )
    links_to_documentation = models.URLField()
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
