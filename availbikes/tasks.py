from celery import shared_task
from django.utils import timezone
from .models import Booking, Bike


@shared_task
def update_bike_availability():
    #get all active bookings whose end time has passed
    expired_bookings = Booking.objects.filter(is_active=True, end_time__lt=timezone.now())

    for booking in expired_bookings:
        booking.is_active = False # mark booking as inactive
        booking.bike.is_available = True # make the bike available again
        booking.bike.save()
        booking.save()