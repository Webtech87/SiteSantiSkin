from email.policy import default

from django.db import models
from drs.models import Dr
from django.utils import timezone

class Podcast(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    link = models.URLField()
    date = models.DateField(default=timezone.now())
    leading_dr = models.ForeignKey(Dr, on_delete=models.CASCADE, related_name='podcasts')

    def __str__(self):
        return self.name
