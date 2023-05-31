from django.contrib import admin
from .models import Event
admin.site.site_header='Event Management Dashboard'

# Register your models here.
admin.site.register(Event)
