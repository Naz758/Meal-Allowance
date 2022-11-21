from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path("", include("meals.urls", namespace='meals')),
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
]
