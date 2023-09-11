from django.contrib import admin
from .models import *

# change the admin site header
admin.site.site_header = 'Minubumwe Administartion'

# change the admin site title
admin.site.site_title = 'Minubumwe Administartion'

# change the admin site index title
admin.site.index_title = 'Minubumwe Administartion'

    
# manage access to allow staff and superuser

admin.site.register(Sector)
admin.site.register(Request)
admin.site.register(SectorApprovedRequest, )
admin.site.register(ApprovedRequest, )


