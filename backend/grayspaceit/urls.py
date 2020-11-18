from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from posts.views import posts
from posts import api

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('posts/', include('posts.urls')),
    path('', include('posts.urls')),
    path('api/comments/', include('posts.api.urls')),
    path('api/auth/', include('authentication.api.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
