from hotels.views import *
from django.urls import path

app_name = 'travelmore'
urlpatterns = [
    path('', home_view, name='home'),
    path('hotel/<slug:slug>/', hotel_info_view.as_view(), name='hotel-info'),
    path('create/hotel/', hotel_create_view.as_view(), name='hotel-create'),
    path('hotel/<slug:slug>/delete/', hotel_delete.as_view(), name='hotel-delete'),
    path('hotel/<slug:slug>/edit/', hotel_modify_view.as_view(), name='hotel-edit'),
    path('feedback/<int:pk>/delete/', feedback_delete.as_view(), name='feedback-delete'),
    path('feedback/<int:pk>/edit/', feedback_edit.as_view(), name='feedback-edit'),
    path('hotel/<slug:slug>/add/room', add_room.as_view(), name='add-room'),
    path('hotel/room/<int:pk>/delete', delete_room.as_view(), name='delete-room'),
    path('hotel/room/<int:pk>/edit', room_modify.as_view(), name='edit-room'),
    path('hotel/room/<int:pk>/info', room_info.as_view(), name='room-info'),
    path('hotel/room/<int:pk>/book', book.as_view(), name='book')
]