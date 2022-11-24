""" Views for the contact app. """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ReviewForm
from .models import Review

from profiles.models import UserProfile


@login_required
def add_review(request):
    """
    A view to return the contact page.
    """
    profile = get_object_or_404(UserProfile, user = request.user)
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            review = review_form.save(commit = False)
            review.user_profile = profile
            review.save()
            messages.success(
                request, f'Thank you for your review.')
            return redirect(reverse('all_reviews'))
        else:
            messages.error(
                request, 'Your form could not be submitted. \
                    Please check the form and try again.')
    else:
        review_form = ReviewForm()

    context = {
        'review_form': review_form,
    }

    return render(request, 'reviews/add_review.html', context)


def all_reviews(request):
    """
    A view to return all Customer reviews page.
    """
    reviews = Review.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, 'reviews/all_reviews.html', context)
