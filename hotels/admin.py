from django.contrib import admin
from hotels.models import Hotel, feedback, location, Room

class Hotel_Admin(admin.ModelAdmin):
    list_display = ('hotelName',)
    prepopulated_fields = {'slug': ('hotelName',)}

admin.site.register(Hotel, Hotel_Admin)
admin.site.register(feedback)
admin.site.register(location)
admin.site.register(Room)
