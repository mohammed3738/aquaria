from cgitb import text
from email import message
from django.db import models

# Create your models here.
class Contact(models.Model):
    srno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField(max_length=55)
    text = models.TextField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name