from hotels.views import home_view, hotel_info_view, hotel_create_view, hotel_delete, hotel_modify_view, feedback_delete
from django.urls import path

app_name = 'travelmore'
urlpatterns = [
    path('', home_view, name='home'),
    path('hotel/<slug:slug>/', hotel_info_view.as_view(), name='hotel-info'),
    path('create/hotel/', hotel_create_view.as_view(), name='hotel-create'),
    path('hotel/<slug:slug>/delete/', hotel_delete.as_view(), name='hotel-delete'),
    path('hotel/<slug:slug>/edit/', hotel_modify_view.as_view(), name='hotel-edit'),
    path('feedback/<int:pk>/delete', feedback_delete.as_view(), name='feedback-delete')
]