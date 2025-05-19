from django.contrib import admin

from mentorships.models import Mentorship


# Register your models here.
class MentorshipAdmin(admin.ModelAdmin):
    class Meta:
        model = Mentorship
        list_display = ('title', 'mentor', 'price', 'type', 'group', 'duration')

admin.site.register(Mentorship, MentorshipAdmin)
