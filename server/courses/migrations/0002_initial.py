# Generated by Django 5.2.1 on 2025-05-16 12:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='coursesenrollment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course_enrollments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddConstraint(
            model_name='coursesenrollment',
            constraint=models.UniqueConstraint(fields=('student', 'course'), name='unique_student_course'),
        ),
    ]
