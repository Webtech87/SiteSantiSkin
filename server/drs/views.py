from rest_framework import viewsets
from users.permissions import IsSuperUser

from .serializers import DrSerializer
from .models import Dr

class DrViewSet(viewsets.ModelViewSet):
    permission_classes = [IsSuperUser]
    queryset = Dr.objects.all()
    serializer_class = DrSerializer

