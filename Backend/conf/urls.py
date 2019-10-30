from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.urls')),
    path('api-auth/', include('rest_framework.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)