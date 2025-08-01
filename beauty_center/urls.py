from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Customize admin site
admin.site.site_header = getattr(settings, 'ADMIN_SITE_HEADER', 'Belle Femme - Administration')
admin.site.site_title = getattr(settings, 'ADMIN_SITE_TITLE', 'Belle Femme Admin')
admin.site.index_title = getattr(settings, 'ADMIN_INDEX_TITLE', 'Panneau d\'Administration')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('services/', include('services.urls')),
    path('appointments/', include('appointments.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])