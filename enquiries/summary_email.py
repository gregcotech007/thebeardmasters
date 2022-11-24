from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


def send_summary_email(enquiry_message):
    """
    Email summary of enquiry form.
    """
    enquiry_email = enquiry_message.email
    subject = render_to_string(
        'enquiries/summary_emails/summary_email_subject.txt')
    body = render_to_string(
        'enquiries/summary_emails/summary_email_body.txt',
        {'enquiry_message': enquiry_message})

    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [enquiry_email]
    )