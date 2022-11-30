from django.db import models

from profiles.models import UserProfile
from bookings.models import Booking


class Review(models.Model):
    """Review model for Customer to leave a review of The Beard Masters"""
    booking = models.ForeignKey(
        Booking, on_delete=models.CASCADE, related_name='reviews')
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=50)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Reviewed by {self.name}"
