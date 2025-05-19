from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('users.urls')),
    path('api/v1/drs/', include('drs.urls')),
    path('api/v1/podcast/', include('podcast.urls')),
    path('api/v1/ms/', include('mentorships.urls')),
    path('api/v1/courses/', include('courses.urls')),
    path('api/v1/post/', include('blog.urls')),
]
