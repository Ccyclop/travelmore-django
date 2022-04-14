from django import forms
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
