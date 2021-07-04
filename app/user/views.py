from .serializers import UserSerializer

from rest_framework import generics


class CreateUserView(generics.CreateAPIView):
    """Create new user in the system"""
    serializer_class = UserSerializer
