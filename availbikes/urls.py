from django.urls import path
from .views import BikeListView, book_bike


urlpatterns = [
    path('bikes/', BikeListView.as_view(), name='bike-list'),
    path('book-bike/<int:bike_id>', book_bike, name='book_bike')
]
