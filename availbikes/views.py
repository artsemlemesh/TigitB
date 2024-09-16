
from rest_framework import generics, status
from .models import Bike, Booking
from .serializers import BikeSerializer, BookingSerializer
from django.utils import timezone
from django.http import JsonResponse
from django.db import transaction
from rest_framework.decorators import api_view
from rest_framework.response import Response
class BikeListView(generics.ListAPIView):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer

# class BikeDetailView(generics.RetrieveAPIView):
#     queryset = Bike.objects.all()
#     serializer_class = BikeSerializer

@transaction.atomic #ensure that 2 users cant book the same bike, locks row in db
@api_view(['POST', 'GET']) #restricts the view to specific HTTP methods/ returns 405 for unsupported
def book_bike(request, bike_id):
    try:
        #lock the bike's row to prevent race conditions
        bike = Bike.objects.select_for_update().get(id=bike_id)
        
        serializer = BookingSerializer(data=request.data)
        # if serializer.is_valid():
        start_time = timezone.now()
        end_time = start_time + timezone.timedelta(hours=2) #rent for 2 hours

        #check if the bike is available
        if bike.is_available and bike.number_of_bikes > 0:
            Booking.objects.create(
                user=request.user, #assuming user is authenticated
                bike=bike,
                start_time=start_time,
                end_time=end_time,
                is_active=True
            )
            #update bike availability and number of bikes
            bike.number_of_bikes -= 1
            if bike.number_of_bikes == 0:
                bike.is_available = False #mark bike as unavailable
            bike.save()

            return JsonResponse({'success': True, 'message': 'Bike booked successfully'}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse({'success': False, 'message': 'Bike is not available'}, status=status.HTTP_400_BAD_REQUEST)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    except Bike.DoesNotExist:
        return JsonResponse({'success': False, 'message': 'Bike not found'}, status=status.HTTP_404_NOT_FOUND)


# #cancellation logic /check later
# def cances_booking(request, booking_id):
#     try:
#         booking = Booking.objects.get(id=booking_id, user=request.user) #allow users to cancell only their own bookings
#         if booking.start_time > timezone.now(): #check if booking hasnt started
#             booking.is_active = False
#             booking.bike.is_available = True
#             booking.bike.save()
#             booking.save()
#             return JsonResponse({'success': True, 'message': 'Booking successfully cancelled'})
#         else:
#             return JsonResponse({'success': False, 'message': 'You cannot cancell an active booking'}, status=400)
#     except Booking.DoesNotExist:
#         return JsonResponse({'success': False, 'message': 'Booking not found'}, status=404)
    

