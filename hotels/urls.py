from hotels.views import home_view
from django.urls import path

app_name = 'travelmore'
urlpatterns = [
    path('', home_view, name='home')
]