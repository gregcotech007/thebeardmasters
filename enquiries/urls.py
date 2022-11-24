from django.urls import path
from . import views

urlpatterns = [
    path('', views.enquiry, name='enquiry'),
    path('manage/', views.manage_enquiry, name='manage_enquiry'),
    path(
        'toggle/<int:enquiry_message_id>/',
        views.toggle_responded, name='toggle_responded'),
]
