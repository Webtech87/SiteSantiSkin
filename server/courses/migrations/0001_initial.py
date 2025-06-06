# Generated by Django 5.2.1 on 2025-05-16 12:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('drs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('type', models.CharField(choices=[('online', 'Online'), ('presence', 'Presence'), ('hybrid', 'Hybrid')], default='online', max_length=10)),
                ('group', models.BooleanField(default=False, max_length=100)),
                ('duration', models.IntegerField()),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='drs.dr')),
            ],
        ),
        migrations.CreateModel(
            name='CoursesEnrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.BooleanField(default=False)),
                ('enrolled_at', models.DateTimeField(auto_now_add=True)),
                ('finish_date', models.DateTimeField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='enrollments', to='courses.course')),
            ],
        ),
    ]
