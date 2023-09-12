from django.contrib import admin
from django.contrib.auth import get_user_model
from django.http.request import HttpRequest
User = get_user_model()


# change admin dashboard tittle
admin.site.site_url = None

admin.site.unregister(User)
admin.site.register(User,)