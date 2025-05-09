from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

from .models import CustomUser
from .serializers import UserSerializer


# Create your views here.
class CustomViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == 'list':
            return [IsAdminUser()]
        if self.action == 'create':
            return [AllowAny()]
        return [IsAuthenticated()]
