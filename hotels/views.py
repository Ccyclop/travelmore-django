from django.shortcuts import render, get_object_or_404, redirect
from hotels.models import Hotel, feedback, Room
from hotels.forms import hotel_Create_Form, location_form, feedback_form
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.views import View
from django.utils.decorators import method_decorator
from django.template.defaultfilters import slugify

def home_view(request):
    return render(request, 'explore.html', {'hotels_list': Hotel.objects.order_by('-created_at').all()})


class hotel_info_view(View):
    form_class = feedback_form
    template_name = 'hotel-info.html'
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        if request.user.is_authenticated:    
            form = self.form_class(initial={'key':'value'})
            return render(request, self.template_name, {
            'hotel': get_object_or_404(Hotel, slug=slug),
            'feedbacks': feedback.objects.filter(hotel__slug=slug),
            'rooms': Room.objects.filter(hotel__slug=slug),
            'form': form
            })
        else:           
            return render(request, self.template_name, {
            'hotel': get_object_or_404(Hotel, slug=slug),
            'feedbacks': feedback.objects.filter(hotel__slug=slug),
            'rooms': Room.objects.filter(hotel__slug=slug),
            })
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save(user=request.user, hotel=Hotel.objects.get(slug=self.kwargs['slug']), commit=True)
            return redirect('travelmore:hotel-info', self.kwargs['slug'])
        else:
            raise ValidationError('Form not Valid')

@method_decorator(login_required, name='dispatch')
class hotel_create_view(View):
    form_class2 = location_form
    form_class = hotel_Create_Form
    initial = {'key': 'value'}
    template_name = 'add-hotel.html'
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        location_form = self.form_class2(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'locationform': location_form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        location_form = self.form_class2(request.POST)
        if form.is_valid() and location_form.is_valid():
            hotel = form.save(request.user, True)
            location = location_form.save(hotel, True)
            return redirect('travelmore:hotel-info', slugify(request.POST['hotelName']))
        else:
            raise ValidationError('Form not Valid')
        return render(request, self.template_name, {'form': form, 'locationform': location_form})
        

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

@method_decorator(login_required, name='dispatch')
class hotel_modify_view(View):
    template_name = 'edit-hotel.html'
    form_class = hotel_Create_Form
    form_class2 = location_form
    
    def get(self, request, *args, **kwargs):
        hotel = get_object_or_404(Hotel, slug=self.kwargs['slug'])
        form = self.form_class(instance=hotel)
        location_form = self.form_class2(instance=hotel.location)
        return render(request, self.template_name, {'form': form, 'locationform': location_form})

    def post(self, request, *args, **kwargs):
        hotel = get_object_or_404(Hotel, slug=self.kwargs['slug'])
        form = self.form_class(request.POST, request.FILES, instance=hotel)
        location_form = self.form_class2(request.POST, instance=hotel.location)
        if request.user == hotel.owner:
            if form.is_valid() and location_form.is_valid():
                hotel = form.save(request.user, True)
                location_form.save(hotel, True)
                return redirect('travelmore:hotel-info', slugify(request.POST['hotelName']))
            else:
                raise ValidationError('Form not Valid')

@method_decorator(login_required, name='dispatch')
class feedback_delete(View):
    template_name = 'hotel-info.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        fb = feedback.objects.get(pk=pk)
        if request.user == fb.user or request.user == fb.hotel.owner:
            fb.delete()
            return redirect('travelmore:hotel-info', fb.hotel.slug)
    
