from django.contrib import admin
from .models import Bus

@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('bus_id', 'route', 'passengers', 'timestamp')
    search_fields = ('bus_id', 'route')
