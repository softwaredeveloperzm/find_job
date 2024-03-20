from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('website.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('company/', include('company.urls')),
    path('resume/', include('resume.urls')),
    path('job/', include('job.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
