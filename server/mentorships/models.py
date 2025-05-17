from django.db import models
from drs.models import Dr
from users.models import CustomUser
from datetime import datetime, timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver


class Type(models.TextChoices):
    ONLINE = ('online', 'Online')
    PRESENCE = ('presence', 'Presence')
    HYBRID = ('hybrid', 'Hybrid')

# Create your models here.
class Mentorship(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mentor = models.ForeignKey(Dr, on_delete=models.CASCADE, related_name='mentorships')
    description = models.TextField()
    type = models.CharField(max_length=10, choices=Type.choices, default=Type.HYBRID)
    group = models.BooleanField(max_length=100)
    duration = models.IntegerField()

    def __str__(self):
        return self.title



class MentorshipEnrollment(models.Model):
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='mentorship_enrollments')
    mentorship = models.ForeignKey(Mentorship, on_delete=models.CASCADE, related_name='enrollments')
    paid = models.BooleanField(default=False)
    enrolled_at = models.DateTimeField(auto_now_add=True)
    finish_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        unique_together = ('student', 'mentorship')

    def save(self, *args, **kwargs):
        if self.enrolled_at and not self.finish_date:
            self.finish_date = self.enrolled_at + timedelta(days=365)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student} - {self.mentorship} ({'PAID' if self.paid else 'UNPAID'})"

@receiver(post_save, sender=MentorshipEnrollment)
def set_finish_date(sender, instance, created, **kwargs):
    if created and not instance.finish_date:
        instance.finish_date = instance.enrolled_at + timedelta(days=365)
        instance.save()