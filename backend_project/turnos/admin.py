from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    # Agregamos 'user' a la lista para ver de quién es el turno
    list_display = ('customer_name', 'date_time', 'status', 'user', 'whatsapp_sent')
    
    # Agregamos 'user' al filtro lateral (útil si tienes varios empleados)
    list_filter = ('user', 'status', 'date_time')
    
    search_fields = ('customer_name', 'customer_phone', 'user__username')