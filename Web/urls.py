from django.contrib import admin
from django.urls import path, include

# from django.urls import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('youloader.urls')),
]
