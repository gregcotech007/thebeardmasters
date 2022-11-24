from django.db import models

from profiles.models import UserProfile


class EnquiryMessage(models.Model):
    """
    Enquiry model for a registered Customer to make an enquiry on their account
    """
    # Set topic options
    ORDER = 'OR'
    WEBSITE = 'WB'
    OTHER = 'OT'
    TOPIC_CHOICES = [
        ('', 'Select Topic *'),
        (ORDER, 'Booking Order'),
        (WEBSITE, 'Our Website'),
        (OTHER, 'Other'),
    ]

    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='enquiries')
    topic = models.CharField(max_length=2, choices=TOPIC_CHOICES)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    responded = models.BooleanField(default=False)

    class Meta:
        """
        Set ordering to ensure newest messages are displayed first.
        """
        ordering = ['-date_created']

    def __str__(self):
        return f'Message from {self.first_name} {self.last_name}'
