from django.urls import path
from .views import DrViewSet

name_app = 'Dr'

list_drs = DrViewSet.as_view({'get': 'list', 'post': 'create'})

CRUD_dr = DrViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy', 'patch': 'partial_update'})


urlpatterns = [
    path('', list_drs, name='list_drs'),
    path('<int:pk>/', CRUD_dr, name='CRUD_dr' ),
]
