from django.urls import path
from django.conf.urls import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name = 'home'),
    path('upload_image/', views.image, name = 'image'),
    path('accounts/profile/', views.profile, name = 'profile'),
    path('profile/', views.otherprofile, name = 'otherprofile'),
    path('search/', views.search,name="search"),
    path('profile/update/', views.update,name='update'),
    path('comment/', views.comment,name='comment'),
    path('like/', views.like,name='like'),
    path('follow/', views.follow,name='follow'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
