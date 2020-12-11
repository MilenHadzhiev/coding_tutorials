from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from coding_tutorials.views import homepage

urlpatterns = [
    path('', homepage, name='homepage'),
    path('accounts/', include('accounts.urls')),
    path('notes/', include('notes.urls')),
    path('tutorials/', include('tutorials.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
