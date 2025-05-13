from django.contrib import admin

from .models import Dr


# Register your models here.
class DrsAdmin(admin.ModelAdmin):
    class Meta:
        model = Dr
        list_display = ('first_name', 'first_name', 'email', 'dr_license')


admin.site.register(Dr, DrsAdmin)


