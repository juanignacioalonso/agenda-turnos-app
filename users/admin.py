from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Extendemos el admin de usuario base para mostrar nuestros campos nuevos
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    # Agregamos 'role' y 'phone_number' a la lista de columnas
    list_display = ['username', 'email', 'role', 'phone_number', 'is_staff']
    
    # Agregamos los campos al formulario de edición
    fieldsets = UserAdmin.fieldsets + (
        ('Información Extra', {'fields': ('role', 'phone_number')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)