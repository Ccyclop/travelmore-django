from django.contrib import admin
from hotels.models import Hotel, Feedback, Location, Room

class Hotel_Admin(admin.ModelAdmin):
    list_display = ('hotelName',)
    prepopulated_fields = {'slug': ('hotelName',)}

admin.site.register(Hotel, Hotel_Admin)
admin.site.register(Feedback)
admin.site.register(Location)
admin.site.register(Room)
