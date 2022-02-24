from django.urls import path, include
from . import views
from .views import *
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework import permissions

router = routers.DefaultRouter()
router.register('users', views.UserView, basename='User')
router.register('gallery', views.GalleryView, basename='Gallery')
router.register('file', views.FileView, basename='File')
router.register('product', views.ProductView, basename='Product')
router.register('section', views.SectionView, basename='Section')
router.register('page', views.PageView, basename='Page')

urlpatterns = [
    path('', include(router.urls)),
    path('docs', include_docs_urls(title='SH Digital Webshop API', public=False)),
    path('schema', get_schema_view(
        title="WebshopAPI",
        description="API for the Webshop",
        version="1.0.0",
        public=True,
    permission_classes=(permissions.AllowAny,),
    ), name='openapi-schema'),    
    path('register/', RegisterView.as_view(), name='auth_register'),
 	
]

