from django.db import IntegrityError
from rest_framework import serializers
from .models import Course, CoursesEnrollment

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'mentor', 'description', 'price', 'type', 'group', 'duration']

    def create(self, validated_data):
        try:
            return Course.objects.create(**validated_data)
        except IntegrityError as e:
            raise serializers.ValidationError({"error": str(e)})

class PaidCoursesEnrollmentSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    class Meta:
        model = CoursesEnrollment
        fields = ['id', 'course', 'enrolled_at', 'finish_date', 'paid']

    def create(self, validated_data):
        request = self.context.get('request')
        course_id = self.context.get('view').kwargs.get('pk')

        try:
            courses = Course.objects.get(pk=course_id)
        except Course.DoesNotExist:
            raise serializers.ValidationError("Mentorship not found.")

        enrollment, created = CoursesEnrollment.objects.get_or_create(
            student=request.user,
            course=courses,
            defaults={'paid': True}
        )

        if not created:
            raise serializers.ValidationError("You are already enrolled in this mentorship.")

        return enrollment