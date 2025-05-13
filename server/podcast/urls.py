from django.urls import path
from .views import PodcastViewSet

app_name = 'podcast'

urlpatterns = [
    path('', PodcastViewSet.as_view(
        {
            'get': 'list',
            'post': 'create'
        }
    )),
    path('<int:pk>/', PodcastViewSet.as_view(
        {
            'get': 'retrieve',
            'patch': 'partial_update',
            'delete': 'destroy',
            'put': 'update',
        }
    )),
]
