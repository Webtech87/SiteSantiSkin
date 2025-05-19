from rest_framework import generics, permissions, viewsets
from .models import Course, CoursesEnrollment
from .serializers import CourseSerializer, PaidCoursesEnrollmentSerializer
from .permitions import CoursesPermitions

# Create your views here.
class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    permission_classes = [CoursesPermitions]
    serializer_class = CourseSerializer

class PaidCoursesListView(viewsets.ModelViewSet):
    serializer_class = PaidCoursesEnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CoursesEnrollment.objects.filter(student=self.request.user, paid=True)
