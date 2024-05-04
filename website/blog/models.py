
from django.db import models

# Create your models here.


class Post(models.Model):
    srno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=5000)
    author = models.CharField(max_length=15)
    slug = models.SlugField(max_length=150)
    timestamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.title + ' by ' + self.author