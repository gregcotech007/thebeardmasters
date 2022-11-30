from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_reviews, name='all_reviews'),
    path('add/<int:booking_id>/', views.add_review, name='add_review'),
]