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
                'max':'5',
                'min': '1'
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
                'placeholder': 'Room Mass',
                'min': '1'
            }),
            'floor': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Which Floor?',
                'min': '1'
            }),
            'beds': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Bed Quantity',
                'min': '1'
            }),
            'bathroom': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Bathtoom Quantity',
                'min': '1'
            }),
            'kitchen': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Kitchen Quantity',
                'min': '1'
            }),
            'price': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Price',
                'min': '1'
            }),
            'balcony': CheckboxInput(attrs={
                'placeholder': 'Balcony'
            }),
            'fire_extinguisher': CheckboxInput(attrs={
                
                'placeholder': 'fire_extinguisher'
            }),
            'minibar': CheckboxInput(attrs={
                
                'placeholder': 'Minibar'
            }),
            'telephone': CheckboxInput(attrs={
                
                'placeholder': 'Telephone'
            }),
            'wifi': CheckboxInput(attrs={
                
                'placeholder': 'Wifi'
            }),
            'tv': CheckboxInput(attrs={

                'placeholder': 'TV'
            }),
        }

class feedback_form(forms.ModelForm):

    def save(self, user, hotel, commit:bool = False):
        feedback = super().save(False)
        feedback.user = user
        feedback.hotel = hotel

        if commit:
            feedback.save()

        return feedback

    class Meta:
        model = feedback
        exclude = ['user', 'hotel']
        widgets = {
            'body': Textarea(attrs={
                'class':'form-control',
                'style':'resize: none; border: 1px solid #ad9f9f;',
                'placeholder': 'Add Comment',
                'rows': '4'
            }),
            'stars': NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Rate Hotel',
                'max':'5',
                'min': '1'
            })
        }
