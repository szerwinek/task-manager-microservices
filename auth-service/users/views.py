from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer


class UserListView(generics.ListAPIView):
    """
    Endpoint zwracający listę użytkowników.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
