from django.db import models
from django.contrib.auth.models import User

class Bike(models.Model):
    header = models.CharField(max_length=255)
    content = models.TextField()
    transmission = models.CharField(max_length=50)
    gears = models.CharField(max_length=50)
    engine = models.CharField(max_length=50)
    seat_height = models.CharField(max_length=50)
    weight = models.CharField(max_length=50)
    power = models.CharField(max_length=50)
    tank_size = models.CharField(max_length=50)
    is_available = models.BooleanField(default=True)
    number_of_bikes = models.IntegerField(default=1)

    def __str__(self):
        return self.header

class Photo(models.Model):
    bike = models.ForeignKey(Bike, related_name='photos', on_delete=models.CASCADE)
    image_url = models.URLField(max_length=200)

    def __str__(self):
        return f"Photo for {self.bike.header}"
    

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_active = models.BooleanField(default=True) #if booking is currently active

    def __str__(self):
        return f'{self.user} booked {self.bike} from {self.start_time} to {self.end_time}'
    
    @staticmethod
    def is_bike_available(bike, start_time, end_time):
        conflicting_bookings = Booking.objects.filter(
            bike=bike,
            is_active=True,
            start_time__lt=end_time,
            end_time__gt=start_time
        )
        return not conflicting_bookings.exists()