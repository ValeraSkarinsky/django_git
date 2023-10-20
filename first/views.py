from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Car
from .serializers import Serializercar, SeriaLizeruser


class CarView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Car.objects.all()
    serializer_class = Serializercar

class CarDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Car.objects.all()
    serializer_class = Serializercar

class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = SeriaLizeruser