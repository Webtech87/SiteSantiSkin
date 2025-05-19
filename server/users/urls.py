from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.urls import path
from .views import CustomViewSet, UpdateProfileView

name_app = 'users'

urlpatterns = [
    path('',
         CustomViewSet.as_view(
             {
                 'get': 'list',
                 'post': 'create',
             }
         ),
         name='users'
         ),
    path('<int:pk>/',
         CustomViewSet.as_view(
             {
                 'get': 'retrieve',
             }
         ),
         name='users_by_id'
         ),
    path('me/', UpdateProfileView.as_view(), name='update_profile'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
