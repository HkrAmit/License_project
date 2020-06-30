from django.contrib import admin
from .models import DriverInfo, CarInfo, Tracker 

class TrackerAdmin(admin.ModelAdmin):
    list_display = ('car', 'driver', 'start_time')


admin.site.register(DriverInfo)
admin.site.register(CarInfo)
admin.site.register(Tracker, TrackerAdmin)
