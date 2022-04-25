from hotels.views import *
from django.urls import path

app_name = 'travelmore'
urlpatterns = [
    path('', home_view, name='home'),
    path('hotel/<slug:slug>/', HotelInfoView.as_view(), name='hotel-info'),
    path('create/hotel/', HotelCreateView.as_view(), name='hotel-create'),
    path('hotel/<slug:slug>/delete/', HotelDelete.as_view(), name='hotel-delete'),
    path('hotel/<slug:slug>/edit/', HotelModify.as_view(), name='hotel-edit'),
    path('feedback/<int:pk>/delete/', FeedbackDelete.as_view(), name='feedback-delete'),
    path('feedback/<int:pk>/edit/', FeedbackModify.as_view(), name='feedback-edit'),
    path('hotel/<slug:slug>/add/room', RoomCreate.as_view(), name='add-room'),
    path('hotel/room/<int:pk>/delete', DeleteRoom.as_view(), name='delete-room'),
    path('hotel/room/<int:pk>/edit', ModifyRoom.as_view(), name='edit-room'),
    path('hotel/room/<int:pk>/info', RoomInfo.as_view(), name='room-info'),
    path('hotel/room/<int:pk>/book', Book.as_view(), name='book')
]