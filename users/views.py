from rest_framework import viewsets
from .models import CustomUser
from .serializers import UserSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API para listar usuarios (útil para llenar el combo de 'Profesionales' en Angular)
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer