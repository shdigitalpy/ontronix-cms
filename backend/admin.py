from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(Gallery)
admin.site.register(Page)
admin.site.register(Section)
admin.site.register(File)
admin.site.register(Product)
admin.site.register(ImageModul)
admin.site.register(TextModul)
admin.site.register(TextImageModul)
admin.site.register(Service)
admin.site.register(Blog)
admin.site.register(Partner)
admin.site.register(Job)

admin.site.site_header = 'API Center'                    # default: "Django Administration"
admin.site.index_title = 'Übersicht Module'                 # default: "Site administration"
admin.site.site_title = 'Django Admin' # default: "Django site admin"