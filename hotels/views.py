from django.shortcuts import render
from hotels.models import Hotel
from django.shortcuts import get_object_or_404

def home_view(request):
    return render(request, 'explore.html', {'hotels_list': Hotel.objects.all()})

def hotel_info_view(request, hotelname : str):
    return render(request, 'hotel-info.html', {'hotel': get_object_or_404(Hotel, hotelName=hotelname)})
