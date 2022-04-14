from django import forms
from django.forms import ModelForm, TextInput, EmailInput, ClearableFileInput, NumberInput, Textarea
from hotels.models import Hotel

class hotelCreateForm(forms.ModelForm):

    def save(self, owner, commit:bool = False):
        hotel = super().save(False)
        hotel.owner = owner

        if commit:
            hotel.save()

        return hotel


    class Meta:
        model = Hotel
        exclude = ['owner']
        widgets = {
            'hotelName': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Hotel Name'
                }),
            'region': TextInput(attrs={
                'class': "form-control",
                'placeholder': 'Region'
                }),
            'price': NumberInput(attrs={
                'class': "form-control",
                'placeholder': 'Price',
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
            })
        }
