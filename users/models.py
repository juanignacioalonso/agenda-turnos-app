from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Definimos los roles
    ADMIN = 'ADMIN'
    USER = 'USER' # O 'USER', como prefieras llamarlo

    ROLE_CHOICES = [
        (ADMIN, 'Administrador'),
        (USER, 'Usuario'),
    ]

    # Agregamos el campo de rol
    role = models.CharField(
        max_length=10, 
        choices=ROLE_CHOICES, 
        default=USER,
        verbose_name="Rol de Usuario"
    )
    
    # Campo opcional para teléfono (muy útil para WhatsApp)
    phone_number = models.CharField(max_length=20, blank=True, null=True, verbose_name="Teléfono")

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"