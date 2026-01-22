from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    # Esto es un truco: muestra el nombre del profesional en lugar de solo su número ID
    professional_name = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Appointment
        fields = '__all__'  # Incluye todos los campos del modelo
        # Alternativamente, podrías listar los campos explícitamente:   
        # fields = ['id', 'customer_name', 'customer_phone', 'date_time', 'status', 'notes', 'whatsapp_sent', 'created_at', 'user', 'professional_name']    