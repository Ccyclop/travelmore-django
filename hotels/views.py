from django.shortcuts import render
from hotels.models import Hotel

def home_view(request):
    return render(request, 'explore.html', {'hotels_list': Hotel.objects.all()})