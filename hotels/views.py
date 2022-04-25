from django.shortcuts import render, get_object_or_404, redirect
from hotels.models import Hotel, Feedback, Room
from hotels.forms import HotelCreateForm, LocationForm, FeedbackForm, RoomForm, SearchForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.views import View
from django.utils.decorators import method_decorator
from django.template.defaultfilters import slugify
from django.core.paginator import Paginator

def home_view(request):

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            p = Paginator(Hotel.objects.filter(slug__contains=slugify(request.POST['search'])).order_by('-created_at'), 9)
            page = request.GET.get('page')
            pagination = p.get_page(page)
            return render(request, 'explore.html', {
                'pagination': pagination,
                'search': SearchForm(initial=request.POST)
            })
    p = Paginator(Hotel.objects.all().order_by('-created_at'), 9)
    page = request.GET.get('page')
    pagination = p.get_page(page)

    return render(request, 'explore.html', {
        'search': SearchForm(initial={'key': 'value'}),
        'pagination': pagination
    })

class HotelInfoView(View):
    form_class = FeedbackForm
    template_name = 'hotel-info.html'
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        slug = self.kwargs['slug']
        if request.user.is_authenticated:    
            form = self.form_class(initial={'key':'value'})
            return render(request, self.template_name, {
            'hotel': get_object_or_404(Hotel, slug=slug),
            'feedbacks': Feedback.objects.filter(hotel__slug=slug),
            'rooms': Room.objects.filter(hotel__slug=slug),
            'form': form
            })
        else:           
            return render(request, self.template_name, {
            'hotel': get_object_or_404(Hotel, slug=slug),
            'feedbacks': Feedback.objects.filter(hotel__slug=slug),
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
class HotelCreateView(View):
    form_class2 = LocationForm
    form_class = HotelCreateForm
    initial = {'key': 'value'}
    template_name = 'add-hotel.html'
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        LocationForm = self.form_class2(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'locationform': LocationForm})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        LocationForm = self.form_class2(request.POST)
        if form.is_valid() and LocationForm.is_valid():
            hotel = form.save(request.user, True)
            location = LocationForm.save(hotel, True)
            return redirect('travelmore:hotel-info', slugify(request.POST['hotelName']))
        else:
            raise ValidationError('Form not Valid')
        return render(request, self.template_name, {'form': form, 'locationform': LocationForm})
        

@method_decorator(login_required, name='dispatch')
class HotelDelete(View):
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
class HotelModify(View):
    template_name = 'edit-hotel.html'
    form_class = HotelCreateForm
    form_class2 = LocationForm
    
    def get(self, request, *args, **kwargs):
        hotel = get_object_or_404(Hotel, slug=self.kwargs['slug'])
        form = self.form_class(instance=hotel)
        LocationForm = self.form_class2(instance=hotel.location)
        return render(request, self.template_name, {'form': form, 'locationform': LocationForm})

    def post(self, request, *args, **kwargs):
        hotel = get_object_or_404(Hotel, slug=self.kwargs['slug'])
        form = self.form_class(request.POST, request.FILES, instance=hotel)
        LocationForm = self.form_class2(request.POST, instance=hotel.location)
        if request.user == hotel.owner:
            if form.is_valid() and LocationForm.is_valid():
                hotel = form.save(request.user, True)
                LocationForm.save(hotel, True)
                return redirect('travelmore:hotel-info', slugify(request.POST['hotelName']))
            else:
                raise ValidationError('Form Not Valid')

@method_decorator(login_required, name='dispatch')
class FeedbackDelete(View):
    template_name = 'hotel-info.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        fb = Feedback.objects.get(pk=pk)
        if request.user == fb.user or request.user == fb.hotel.owner:
            fb.delete()
            return redirect('travelmore:hotel-info', fb.hotel.slug)
    
@method_decorator(login_required, name='dispatch')
class FeedbackModify(View):
    template_name = 'feedback-edit.html'
    form_class = FeedbackForm

    def get(self, request, *args, **kwargs):
        fb = Feedback.objects.get(pk=self.kwargs['pk'])
        form = self.form_class(instance=fb)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request ,*args, **kwargs):
        fb = Feedback.objects.get(pk=self.kwargs['pk'])
        hotel = fb.hotel
        form = self.form_class(request.POST, instance=fb)
        if request.user == fb.user:
            if form.is_valid():
                fb = form.save(user=request.user, hotel=hotel, commit=True)
                return redirect('travelmore:hotel-info', hotel.slug)
            else:
                raise ValidationError('Form Not Valid')

@method_decorator(login_required, name='dispatch')
class RoomCreate(View):
    form_class = RoomForm
    template_name = 'add-room.html'
    
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial={'key': 'value'})
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        hotel = Hotel.objects.get(slug=self.kwargs['slug'])
        if form.is_valid():
            form = form.save(hotel=hotel, commit=True)
            return redirect('travelmore:hotel-info', self.kwargs['slug'])
        else:
            raise ValidationError('Form Not Valid')

@method_decorator(login_required, name='dispatch')
class DeleteRoom(View):
    template_name = 'hotel-info.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
        
    def post(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        room = Room.objects.get(pk=pk)
        hotel = room.hotel
        if request.user == room.hotel.owner:
            room.delete()
            return redirect('travelmore:hotel-info', hotel.slug)

@method_decorator(login_required, name='dispatch')
class ModifyRoom(View):
    template_name = 'edit-room.html'
    form_class = RoomForm

    def get(self, request, *args, **kwargs):
        room = Room.objects.get(pk=self.kwargs['pk'])
        form = self.form_class(instance=room)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        room = Room.objects.get(pk=self.kwargs['pk'])
        hotel = room.hotel
        form = self.form_class(request.POST, request.FILES, instance=room)
        if form.is_valid():
            form.save(hotel=hotel, commit=True)
            return redirect('travelmore:hotel-info', hotel.slug)
        else:
            raise ValidationError('Form Not Valid')

class RoomInfo(View):
    template_name = 'room-info.html'

    def get(self, request, *args, **kwargs):
        room = Room.objects.get(pk=self.kwargs['pk'])
        return render(request, self.template_name, {'room': room})

@method_decorator(login_required, name='dispatch')
class Book(View):
    template_name = 'book.html'
    form_class = RoomForm

    def get(self, request, *args, **kwargs):
        room = Room.objects.get(pk=self.kwargs['pk'])
        return render(request, self.template_name, {'room': room})

    def post(self, request, *args, **kwargs):
        room = Room.objects.get(pk=self.kwargs['pk'])
        hotel = room.hotel
        form = self.form_class(instance=room)
        form.save(hotel=hotel, booked=True, commit=True)
        return redirect('travelmore:hotel-info', room.hotel.slug)
        


