from django.db import models

from config import settings


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=255)
    creater = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    description = models.TextField(null=True, blank=True)
    event_location = models.CharField(max_length=255)
    date = models.DateTimeField()
    image_url = models.CharField(max_length=255)
