from django.urls import path
from .views import CoursesViewSet, PaidCoursesListView

name_app = 'courses'

urlpatterns = [
    path('', CoursesViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='course-list'),

    path('<int:pk>/', CoursesViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='course-detail'),

    path('my/', PaidCoursesListView.as_view(
        {
            'get': 'list',
        }
    ), name='my_course-list'),

    path('<int:pk>/buy/', PaidCoursesListView.as_view(
        {
            'post': 'create',
        }
    ), name='buy_course')
]
