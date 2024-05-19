from django.db import models
from authentication.models import User

# Create your models here.


class Task(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    task = models.TextField()
    completed = models.BooleanField(default=False)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

