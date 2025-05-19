from django.db import models
from drs.models import Dr


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Dr, on_delete=models.CASCADE, related_name='posts')