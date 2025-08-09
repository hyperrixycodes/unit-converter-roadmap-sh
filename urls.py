from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('length/', views.length, name='length'),
    path('weight/', views.weight, name='weight'),
    path('temperature/', views.temperature, name='temperature'),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
