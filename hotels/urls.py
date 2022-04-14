from hotels.views import home_view, hotel_info_view, hotel_create_view
from django.urls import path

app_name = 'travelmore'
urlpatterns = [
    path('', home_view, name='home'),
    path('hotel/<str:hotelname>/', hotel_info_view, name='hotel-info'),
    path('create/hotel/', hotel_create_view, name='hotel-create'),
    
]