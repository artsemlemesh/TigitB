from django.shortcuts import render
from rest_framework import generics
from .serializers import MainTabSerializer
from .models import MainTab

class TabsView(generics.ListAPIView):
    serializer_class = MainTabSerializer
    queryset = MainTab.objects.all()
    