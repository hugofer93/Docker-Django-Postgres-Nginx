from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models

# register the User model
admin.site.register(models.User, UserAdmin)


# Custom AdminSite
class AdminSite(admin.AdminSite):
    admin.AdminSite.site_header = 'Wogo App'
    admin.AdminSite.site_title = admin.AdminSite.site_header
