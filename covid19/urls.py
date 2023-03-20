
from django.contrib import admin
from django.urls import path, include
import Covid.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(Covid.urls))
]
