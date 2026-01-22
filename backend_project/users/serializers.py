from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        # Solo enviamos datos seguros, nunca la contraseña
        fields = ['id', 'username', 'first_name', 'last_name', 'role', 'phone_number']