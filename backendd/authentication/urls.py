from django.urls import path
from .views import login_view, logout_view, user_profile

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('user-profile/', user_profile, name='user-profile'),

]
