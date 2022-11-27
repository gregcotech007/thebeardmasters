"""Views for Subscribers form & Newsletter"""
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.mail import send_mass_mail
from django_pandas.io import read_frame
from .models import Subscriber
from .forms import SubscriberForm, NewsletterForm


def subscribe(request):
    """Subscribers Form View"""
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        email = request.POST.get('email', None)
        if form.is_valid():
            subscribe_user = Subscriber.objects.filter(email=email).first()
            if subscribe_user:
                messages.error(
                    request, f"{email} email address is already subscribed.")
                return redirect(request.META.get("HTTP_REFERER", "/"))
            else:
                form.save()
                messages.success(request, 'Subscription Successful')
                return redirect(request.META.get("HTTP_REFERER", "/"))
    else:
        form = SubscriberForm()
    context = {
        'form': form,
    }
    return render(request, 'newsletter/newsletter.html', context)


@login_required
def newsletter(request):
    """Newsletter Form View & Email to Subscribers"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only Administrators are authorised to access Newsletter')
        return redirect(reverse('home'))

    emails = Subscriber.objects.all()
    email_host = settings.DEFAULT_FROM_EMAIL
    data_frame = read_frame(emails, fieldnames=['email'])
    mail_list = data_frame['email'].values.tolist()

    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            title = form.cleaned_data.get('title')
            message = form.cleaned_data.get('message')
            body = render_to_string(
                'newsletter/newsletter_emails/newsletter_body.txt',
                {'message': message})
            email = [(title, body, email_host, [recipient])
                     for recipient in mail_list]
            send_mass_mail(email)

            messages.success(request, 'Newsletter Successfully Sent')
            return redirect('newsletter')
    else:
        form = NewsletterForm()

    context = {
        'form': form,
    }
    return render(request, 'newsletter/newsletter.html', context)