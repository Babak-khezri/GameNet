
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gamenet.urls')),
    path('account/', include('account.urls')),
    path('reserve/', include('reserve.urls')),
    path('system/', include('system.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
