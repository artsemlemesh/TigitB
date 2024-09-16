

from rest_framework import serializers
from .models import Bike, Photo, Booking

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'image_url']

class BikeSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Bike
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        # check if the bike is available during the requested time
        bike = data.get('bike')
        start_time = data.get('start_time')
        end_time = data.get('end_time')

        if start_time >= end_time:
            raise serializers.ValidationError('end time must be after start time.')
        
        if not Booking.is_bike_available(bike, start_time, end_time):
            raise serializers.ValidationError('bike is not available for the requested time')
        
        return data