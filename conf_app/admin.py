from django.contrib import admin
# Register your models here.
from .models import Company, ConferenceRoom, CalendarEvent

admin.site.register(Company)
admin.site.register(ConferenceRoom)
admin.site.register(CalendarEvent)