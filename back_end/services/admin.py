from django.contrib import admin
from .models import *

# change the admin site header
admin.site.site_header = 'Minubumwe Sheltering Provision For Genocide Survivors'

# change the admin site title if 
admin.site.site_title = 'Administartion'

# change the admin site index title
admin.site.index_title = 'Minubumwe Administartion'

    
# manage access to allow staff and superuser

class RequestAdmin(admin.ModelAdmin):
    list_display = ( 'message', 'sector','social_status_class', 'approved')
    list_filter = ('sector',)
    search_fields = ( 'sector', 'social_status_class')
    list_per_page = 25


admin.site.register(Sector)
admin.site.register(Request, RequestAdmin)
admin.site.register(SectorApprovedRequest,RequestAdmin )
admin.site.register(ApprovedRequest, RequestAdmin)


