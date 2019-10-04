from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("hospitals.urls",), name="index"),
    path('donors/', include("donors.urls", namespace="donors"))
]
