from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    class Meta:
        model = CustomUser
        list_display = ('email', 'is_staff', 'is_active')
        search_fields = ('email', 'username')
        ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)