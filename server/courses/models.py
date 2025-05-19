from django.db import models
from drs.models import Dr
from users.models import CustomUser
from datetime import datetime, timedelta

class Type(models.TextChoices):
    ONLINE = ('online', 'Online')
    PRESENCE = ('presence', 'Presence')
    HYBRID = ('hybrid', 'Hybrid')

class Course(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mentor = models.ForeignKey(Dr, on_delete=models.CASCADE, related_name='courses')
    description = models.TextField()
    type = models.CharField(max_length=10, choices=Type.choices, default=Type.ONLINE)
    group = models.BooleanField(max_length=100, default=False)
    duration = models.IntegerField()

    def __str__(self):
        return self.title


class CoursesEnrollment(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='course_enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    paid = models.BooleanField(default=False)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    finish_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['student', 'course'], name='unique_student_course')
        ]

    def save(self, *args, **kwargs):
        if self.enrolled_at and not self.finish_date:
            self.finish_date = self.enrolled_at + timedelta(days=365)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student} - {self.course} ({'PAID' if self.paid else 'UNPAID'})"