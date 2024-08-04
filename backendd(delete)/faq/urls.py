from .views import TabsView
from django.urls import path



urlpatterns = [
    path('tabs/', TabsView.as_view(), name='tabs-list')
]
