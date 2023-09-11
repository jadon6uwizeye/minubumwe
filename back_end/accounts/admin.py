from django.contrib import admin
from django.contrib.auth import get_user_model
from django.http.request import HttpRequest
User = get_user_model()

# change the admin site header
admin.site.site_header = 'Minubumwe Administartion'

# change the admin site title
admin.site.site_title = 'Minubumwe Administartion'

# change the admin site index title
admin.site.index_title = 'Minubumwe Administartion'

# change admin dashboard tittle
admin.site.site_url = None

admin.site.unregister(User)
admin.site.register(User,)