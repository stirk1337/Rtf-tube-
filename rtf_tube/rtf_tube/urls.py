from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('video.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', include('users.urls'), name='register')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + \
    static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)
