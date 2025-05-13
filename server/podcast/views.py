from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import PodcastSerializer
from podcast.models import Podcast


# Create your views here.
class PodcastViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer