from django.db import models

# Create your models here.
from django.db import models

class UserMessage(models.Model):
    name = models.CharField(max_length=100, default=" ")
    email = models.EmailField(default=" ")
    phone = models.CharField(max_length=40, default=" ")
    subject = models.CharField(max_length=200, default=" ")
    message = models.TextField(default=" ")

    def __str__(self):
        return f"Message from {self.name}"
