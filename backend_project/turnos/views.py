from rest_framework import viewsets
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all().order_by('date_time')
    serializer_class = AppointmentSerializer

    # Aquí en el futuro agregaremos la lógica de:
    # "Si es cliente, solo ve sus turnos. Si es admin, ve todos."