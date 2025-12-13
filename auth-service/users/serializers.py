from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer użytkownika – expose tylko podstawowe dane.
    """
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
