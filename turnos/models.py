from django.db import models
from django.conf import settings # <--- Importante para referenciar al usuario
from django.core.exceptions import ValidationError
from django.utils import timezone

def validar_fecha_futura(value):
    if value < timezone.now():
        raise ValidationError("No se puede agendar un turno en el pasado.")

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pendiente'),
        ('CONFIRMED', 'Confirmado'),
        ('CANCELLED', 'Cancelado'),
    ]

    # --- NUEVO CAMPO: LA RELACIÓN ---
    # Esto dice: "Este turno pertenece a este Usuario"
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, # Apunta a tu CustomUser
        on_delete=models.CASCADE, # Si borras al usuario, se borran sus turnos
        related_name='appointments', # Para buscar al revés: usuario.appointments.all()
        verbose_name="Profesional a cargo"
    )

    # Datos del cliente (Quien recibe el servicio)
    customer_name = models.CharField(max_length=100, verbose_name="Nombre Cliente")
    customer_phone = models.CharField(max_length=20, verbose_name="Teléfono")
    
    date_time = models.DateTimeField(
        verbose_name="Fecha y Hora",
        validators=[validar_fecha_futura]
    )
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    notes = models.TextField(blank=True, null=True)
    whatsapp_sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"

    def __str__(self):
        return f"{self.customer_name} ({self.date_time}) - Prof: {self.user.username}"