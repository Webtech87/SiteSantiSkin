from rest_framework.permissions import AllowAny

from .permitions import MentorShipPermitions
from rest_framework import viewsets, generics, permissions
from .models import Mentorship, MentorshipEnrollment
from .serializers import MentorshipSerializer, PaidMentorshipEnrollmentSerializer

class MentorshipViewSet(viewsets.ModelViewSet):
    queryset = Mentorship.objects.all()
    permission_classes = [MentorShipPermitions]
    serializer_class = MentorshipSerializer


class PaidMentorshipListView(generics.ListAPIView):
    serializer_class = PaidMentorshipEnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MentorshipEnrollment.objects.filter(student=self.request.user, paid=True)
