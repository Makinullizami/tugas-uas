# lizam_store/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('aplikasi_utama.urls')),
    path('admin/', admin.site.urls),
]
