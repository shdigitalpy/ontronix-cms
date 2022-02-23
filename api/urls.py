from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/token', obtain_auth_token, name='api-token-auth'),
    path('', include('backend.urls')),
    path('', include('cms.urls')),
    path('accounts/', include('allauth.urls')),
]
