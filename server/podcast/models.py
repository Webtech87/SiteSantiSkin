from django.db import models

class Podcast(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='podcasts/')
    link = models.URLField()
    date = models.DateField()
    leading_actor = models.CharField(max_length=100)
    def __str__(self):
        return self.name
