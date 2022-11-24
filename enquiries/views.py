from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import EnquiryForm
from .models import EnquiryMessage
from .summary_email import send_summary_email
from profiles.models import UserProfile

@login_required
def enquiry(request):
    """
    A view to return the enquiry page.
    """
    profile = get_object_or_404(UserProfile, user = request.user)
    if request.method == 'POST':
        enquiry_form = EnquiryForm(request.POST)
        if enquiry_form.is_valid():
            enquiry_message = enquiry_form.save(commit=False)
            enquiry_message.user_profile = profile
            enquiry_message.save()
            send_summary_email(enquiry_message)
            messages.success(
                request, f'We have received your message. \
                    A summary has been sent to {enquiry_message.email}. \
                    A Customer Service Advisor will be in touch shortly.')
            return redirect(reverse('home'))
        else:
            messages.error(
                request, 'Your message could not be submitted. \
                    Please check the form and try again.')
    else:
        enquiry_form = EnquiryForm()

    context = {
        'enquiry_form': enquiry_form,
    }

    return render(request, 'enquiries/enquiry.html', context)


@login_required
def manage_enquiry(request):
    """
    List customer enquiry messages for the store admin.
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only Administrators are authorised.')
        return redirect(reverse('home'))

    enquiry_messages = EnquiryMessage.objects.all()

    context = {
        'enquiry_messages': enquiry_messages
    }

    return render(request, 'enquiries/manage_enquiry.html', context)


@login_required
def toggle_responded(request, enquiry_message_id):
    """
    Toggle the responded field of an individual contact message.
    """
    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only Administrators are authorised.')
        return redirect(reverse('home'))

    enquiry_message = get_object_or_404(EnquiryMessage, pk=enquiry_message_id)
    enquiry_message.responded = not enquiry_message.responded
    enquiry_message.save()

    return redirect(reverse('manage_enquiry'))
