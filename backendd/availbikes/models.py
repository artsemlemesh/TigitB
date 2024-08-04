from django.db import models


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

    def __str__(self):
        return self.header

class Photo(models.Model):
    bike = models.ForeignKey(Bike, related_name='photos', on_delete=models.CASCADE)
    image_url = models.URLField(max_length=200)

    def __str__(self):
        return f"Photo for {self.bike.header}"