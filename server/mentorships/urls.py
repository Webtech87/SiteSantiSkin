from django.urls import path
from .views import MentorshipViewSet, PaidMentorshipListView

name_app = 'Mentorships'

urlpatterns = [
    path('', MentorshipViewSet.as_view({
        'get': 'list',
        'post': 'create',
    }), name='mentorship-list-create'),

    path('<int:pk>/', MentorshipViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy',
    }), name='mentorship-detail'),
    path('<int:pk>/buy/', PaidMentorshipListView.as_view(
        {
            'post': 'create',
        }
    ), name='buy_mentorship'),

    path('my/', PaidMentorshipListView.as_view(
        {
            'get': 'list',
        }
    ), name='my_mentorship-list'),
]
