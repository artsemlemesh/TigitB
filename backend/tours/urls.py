from django.urls import path
from .views import TourListCreateView, TourDetailView

urlpatterns = [
    path('tours/', TourListCreateView.as_view(), name='tour-list-create'),
    path('tours/<int:pk>/', TourDetailView.as_view(), name='tour-detail'),
]