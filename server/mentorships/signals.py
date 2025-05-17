from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta
from .models import MentorshipEnrollment

@receiver(post_save, sender=MentorshipEnrollment)
def set_finish_date(sender, instance, created, **kwargs):
    if created and not instance.finish_date:
        instance.finish_date = instance.enrolled_at + timedelta(days=365)
        instance.save()