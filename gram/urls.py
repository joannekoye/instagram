from django.urls import path
from django.conf.urls import static
from django.conf import settings
from . import views

urlpatterns = [

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)