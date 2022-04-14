from django.shortcuts import render, get_object_or_404, redirect
from hotels.models import Hotel
from hotels.forms import hotelCreateForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError


def home_view(request):
    return render(request, 'explore.html', {'hotels_list': Hotel.objects.all()})


def hotel_info_view(request, hotelname: str):
    return render(request, 'hotel-info.html', {'hotel': get_object_or_404(Hotel, hotelName=hotelname)})


def hotel_create_view(request):

    if not request.user.is_authenticated:
        return redirect('travelmore:home')
    else:
        if request.method == 'POST':
            form = hotelCreateForm(request.POST, request.FILES)
            if form.is_valid():
                form.save(request.user, True)
                
                return redirect('travelmore:hotel-info', request.POST['hotelName'])
            else:
                raise ValidationError('Form not Valid')
        
                


        return render(request, 'add-hotel.html', {'form': hotelCreateForm()})
