from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import User_info

# Register your models here.

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class User_infoInline(admin.StackedInline):
    model = User_info
    can_delete = False
    verbose_name_plural = 'userinfo'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (User_infoInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)