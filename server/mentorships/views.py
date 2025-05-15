from .permitions import MentorShipPermitions
from rest_framework import viewsets, generics, permissions
from .models import Mentorship, MentorshipEnrollment
from users.permissions import IsSuperUser
from .serializers import MentorshipSerializer, PaidMentorshipEnrollmentSerializer


# Create your views here.

class MentorshipViewSet(viewsets.ModelViewSet):
    queryset = Mentorship.objects.all()
    permission_classes = [MentorShipPermitions]
    serializer_class = MentorshipSerializer


class PaidMentorshipListView(generics.ListAPIView):
    serializer_class = PaidMentorshipEnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return MentorshipEnrollment.objects.filter(student=self.request.user, paid=True)
