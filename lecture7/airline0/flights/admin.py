from django.contrib import admin

from .models import *

# Register your models here.
class FlightAdmin(admin.ModelAdmin):
    # changing what is displayed when loading the Flights
    list_display = ("id", "origin", "destination", "duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",)

admin.site.register(Airport)
# configuring Flight with the FlightAdmin configurations
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
