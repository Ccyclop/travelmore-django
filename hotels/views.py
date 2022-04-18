from django.shortcuts import render, get_object_or_404, redirect
from hotels.models import Hotel
from hotels.forms import hotel_Create_Form
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.views import View
from django.utils.decorators import method_decorator
from django.template.defaultfilters import slugify

def home_view(request):
    return render(request, 'explore.html', {'hotels_list': Hotel.objects.order_by('-created_at').all()})


def hotel_info_view(request, slug):
    return render(request, 'hotel-info.html', {'hotel': get_object_or_404(Hotel, slug=slug)})

@method_decorator(login_required, name='dispatch')
class hotel_create_view(View):
    form_class = hotel_Create_Form
    initial = {'key': 'value'}
    template_name = 'add-hotel.html'
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save(request.user, True)
            return redirect('travelmore:hotel-info', slugify(request.POST['hotelName']))
        else:
            raise ValidationError('Form not Valid')
        return render(request, self.template_name, {'form': form})
        

@method_decorator(login_required, name='dispatch')
class hotel_delete(View):
    template_name = 'delete.html'

    def get(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        return render(request, self.template_name, {'hotel': get_object_or_404(Hotel, slug=slug)})
    
    def post(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        hotel = get_object_or_404(Hotel, slug=slug)
        if request.user == hotel.owner:
            hotel.delete()
            return redirect('travelmore:home')
    
