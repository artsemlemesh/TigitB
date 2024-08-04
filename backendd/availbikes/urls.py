from django.urls import path
from .views import BikeListView


urlpatterns = [
    path('bikes/', BikeListView.as_view(), name='bike-list')
]
