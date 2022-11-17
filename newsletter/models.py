"""Newsletter Models"""
from django.db import models


class Subscriber(models.Model):
    """Subscribers emails Model"""
    email = models.EmailField(null=True)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email}"


class Newsletter(models.Model):
    """Newletters Model"""
    title = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"
