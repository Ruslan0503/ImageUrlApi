from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from django.urls import path
from .views import ImageUploadView

urlpatterns = [
    path('', ImageUploadView.as_view(), name='image-upload'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
