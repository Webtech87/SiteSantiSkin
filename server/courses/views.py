from rest_framework import generics, permissions, viewsets
from .models import Course, CoursesEnrollment
from .serializers import CourseSerializer, PaidCoursesEnrollmentSerializer
from mentorships.permitions import MentorShipPermitions

# Create your views here.
class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    permission_classes = [MentorShipPermitions]
    serializer_class = CourseSerializer


class PaidCoursesListView(generics.ListAPIView):
    serializer_class = PaidCoursesEnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CoursesEnrollment.objects.filter(student=self.request.user, paid=True)
