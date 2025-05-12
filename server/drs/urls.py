from django.urls import path
from .views import DrViewSet

name_app = 'Dr'

urlpatterns = [
    path('', DrViewSet.as_view({'get': 'list', 'post': 'create'})),
]