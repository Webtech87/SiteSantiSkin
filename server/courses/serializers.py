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
    mentorship = CourseSerializer()
    class Meta:
        model = CoursesEnrollment
        fields = ['id', 'mentorship', 'enrolled_at', 'finish_date', 'paid']