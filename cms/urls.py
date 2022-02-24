from django.urls import path, include
from . import views


urlpatterns = [
    #cms
    path('cms/', views.cms, name='cms'),
    
    #login / logout
    path('cms/login', views.login_user, name='login_user'),
    path('cms/logout_user', views.logout_user, name='logout_user'), 
    path('cms/kunden', views.cms_kunden, name='cms_kunden'),

    #files
    path('cms/pdf', views.cms_pdf, name='cms_pdf'),
    path('cms/pdf/upload', views.cms_pdf_upload, name='cms_pdf_upload'),
    path('cms/pdf/edit/<int:pk>', views.cms_pdf_edit, name='cms_pdf_edit'),


    #pages
    path('cms/pages', views.cms_pages, name='cms_pages'),

    #products
    path('cms/produkte', views.cms_produkte, name='cms_produkte'),
    path('cms/produkte/erfassen', views.cms_produkte_erfassen, name='cms_produkte_erfassen'),
 	path('cms/produkte/bearbeiten/<int:pk>', views.cms_produkte_bearbeiten, name='cms_produkte_bearbeiten'),
    path('cms/produkte/löschen/<int:pk>', views.cms_produkte_löschen, name='cms_produkte_löschen'),
    path('cms/produkte/gallery/<int:pk>', views.cms_gallery_images, name='cms_gallery_images'),
    path('cms/produkte/gallery/add/<int:pk>', views.cms_gallery_image_add, name='cms_gallery_image_add'),
    path('cms/produkte/gallery/löschen/<int:ppk>/<int:pk>', views.cms_gallery_image_delete, name='cms_gallery_image_delete'),

    #service
    path('cms/service', views.cms_service, name='cms_service'),
    path('cms/service/erfassen', views.cms_service_erfassen, name='cms_service_erfassen'),
    path('cms/service/bearbeiten/<int:pk>', views.cms_service_bearbeiten, name='cms_service_bearbeiten'),
    path('cms/service/löschen/<int:pk>', views.cms_service_löschen, name='cms_service_löschen'),

    #orders
    path('cms/bestellungen', views.cms_orders, name='cms_orders'),

]

