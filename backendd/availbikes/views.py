
from rest_framework import generics
from .models import Bike
from .serializers import BikeSerializer

class BikeListView(generics.ListAPIView):
    queryset = Bike.objects.all()
    serializer_class = BikeSerializer

# class BikeDetailView(generics.RetrieveAPIView):
#     queryset = Bike.objects.all()
#     serializer_class = BikeSerializer