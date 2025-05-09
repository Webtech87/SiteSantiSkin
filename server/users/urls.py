from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from django.urls import path
from .views import CustomViewSet

name_app = 'users'

urlpatterns = [
    path('',
         CustomViewSet.as_view(
            {
                'get': 'list',
                 'post': 'create',
                 'put': 'update',
                 'delete': 'destroy'
            }
        ),
         name='users'
    ),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
