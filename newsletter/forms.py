"""Forms for Newsletters & Subscribers"""
from django import forms
from .models import Subscriber, Newsletter


class SubscriberForm(forms.ModelForm):
    """ Subscribers Form """
    class Meta:
        model = Subscriber
        fields = ['email', ]


class NewsletterForm(forms.ModelForm):
    """ Newsletter Form """
    class Meta:
        model = Newsletter
        fields = [
            'title',
            'message',
            ]
