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
    path('cms/pages/sections/<int:pk>', views.cms_section_detail, name="cms_section_detail"),
    path('cms/pages/sections/modules/<int:pk>/<str:module>/<int:section_pk>', views.cms_module_detail, name="cms_module_detail"),
    path('cms/pages/sections/modules/bearbeiten/<int:pk>/<str:module>/<int:section_pk>/', views.cms_module_bearbeiten, name="cms_module_bearbeiten"),

    #products
    path('cms/produkte', views.cms_produkte, name='cms_produkte'),
    path('cms/produkte/erfassen', views.cms_produkte_erfassen, name='cms_produkte_erfassen'),
 	path('cms/produkte/bearbeiten/<int:pk>', views.cms_produkte_bearbeiten, name='cms_produkte_bearbeiten'),
    path('cms/produkte/löschen/<int:pk>', views.cms_produkte_löschen, name='cms_produkte_löschen'),
    path('cms/produkte/gallery/<int:pk>', views.cms_gallery_images, name='cms_gallery_images'),
    path('cms/produkte/gallery/add/<int:pk>', views.cms_gallery_image_add, name='cms_gallery_image_add'),
    path('cms/produkte/gallery/löschen/<int:ppk>/<int:pk>', views.cms_gallery_image_delete, name='cms_gallery_image_delete'),

    #partner
    path('cms/partner', views.cms_partner, name='cms_partner'),
    path('cms/partner/erfassen', views.cms_partner_erfassen, name='cms_partner_erfassen'),
    path('cms/partner/bearbeiten/<int:pk>', views.cms_partner_bearbeiten, name='cms_partner_bearbeiten'),
    path('cms/partner/löschen/<int:pk>', views.cms_partner_löschen, name='cms_partner_löschen'),


    #service
    path('cms/service', views.cms_service, name='cms_service'),
    path('cms/service/erfassen', views.cms_service_erfassen, name='cms_service_erfassen'),
    path('cms/service/bearbeiten/<int:pk>', views.cms_service_bearbeiten, name='cms_service_bearbeiten'),
    path('cms/service/löschen/<int:pk>', views.cms_service_löschen, name='cms_service_löschen'),

    #blog
    path('cms/blog', views.cms_blog, name='cms_blog'),
    path('cms/blog/erfassen', views.cms_blog_erfassen, name='cms_blog_erfassen'),
    path('cms/blog/bearbeiten/<int:pk>', views.cms_blog_bearbeiten, name='cms_blog_bearbeiten'),
    path('cms/blog/löschen/<int:pk>', views.cms_blog_löschen, name='cms_blog_löschen'),

    #job
    path('cms/jobs/', views.cms_jobs, name='cms_jobs'),
    path('cms/job/erfassen', views.cms_jobs_erfassen, name='cms_jobs_erfassen'),
    path('cms/job/bearbeiten/<int:pk>', views.cms_jobs_bearbeiten, name='cms_jobs_bearbeiten'),
    path('cms/job/löschen/<int:pk>', views.cms_jobs_löschen, name='cms_jobs_löschen'),
]

