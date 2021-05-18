from django.db import models
from django.contrib.auth.models import User


class Events(models.Model):
    title = models.CharField(max_length=200)
    about_event = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    organiser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title






