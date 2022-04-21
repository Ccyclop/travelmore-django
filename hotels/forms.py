from django import forms
from django.forms import TextInput, EmailInput, ClearableFileInput, NumberInput, Textarea, CheckboxInput
from hotels.models import Hotel, location, Room, feedback
from django.template.defaultfilters import slugify

class hotel_Create_Form(forms.ModelForm):

    def save(self, owner, commit:bool = False):
        hotel = super().save(False)
        hotel.owner = owner
        hotel.slug = slugify(hotel.hotelName)

        if commit:
            hotel.save()

        return hotel


    class Meta:
        model = Hotel
        exclude = ['owner', 'slug']
        widgets = {
            'hotelName': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Hotel Name'
                }),
            'stars': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Stars',
                }),
            'thumbnail': ClearableFileInput(attrs={
                'class': "form-control",
                'title': 'Thumbnail Photo'
                }),
            'hotelImage': ClearableFileInput(attrs={
                'class': "form-control",
                'title': 'Hotel Cover Photo'
                }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description',
                'cols': '10',
                'rows': '10'
                }),  
                
        }

class location_form(forms.ModelForm):

    def save(self, hotel, commit:bool = False):
        location = super().save(False)
        location.hotel = hotel

        if commit:
            location.save()

        return location

    class Meta:
        model = location
        exclude = ['hotel',]
        widgets = {
            'region': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Region'
                }),
            'address': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Address'
                }),
        }

class room_form(forms.ModelForm):

    def save(self, hotel, commit:bool = False):
        room = super().save(False)
        room.hotel = hotel

        if commit:
            room.save()

        return room

    class Meta:
        model = Room
        exclude = ['hotel',]
        widgets = {
            'room_image1': ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'room_image2': ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'room_image3': ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'room_image4': ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'room_mass': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Room Mass'
            }),
            'floor': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Which Floor?'
            }),
            'beds': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Bed Quantity'
            }),
            'bathroom': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Bathtoom Quantity'
            }),
            'kitchen': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Kitchen Quantity'
            }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Price'
            }),
            'balcony': CheckboxInput(attrs={
                'class': 'form-control',
                'placeholder': 'Balcony'
            }),
            'fire_extinguisher': CheckboxInput(attrs={
                'class': 'form-control',
                'placeholder': 'fire_extinguisher'
            }),
            'minibar': CheckboxInput(attrs={
                'class': 'form-control',
                'placeholder': 'Minibar'
            }),
            'telephone': CheckboxInput(attrs={
                'class': 'form-control',
                'placeholder': 'Telephone'
            }),
            'wifi': CheckboxInput(attrs={
                'class': 'form-control',
                'placeholder': 'Wifi'
            }),
            'tv': CheckboxInput(attrs={
                'class': 'form-control',
                'placeholder': 'TV'
            }),
        }