from django.contrib import admin
from django.urls import path
from Beranda.views import halaman


urlpatterns = [
    path('admin/', admin.site.urls),
    path('halaman/',halaman),
]
