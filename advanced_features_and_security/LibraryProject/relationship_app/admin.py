from django.contrib import admin

"""
Modify the Django admin to support the custom user model, ensuring that administrators can 
manage users effectively through the Django admin interface.
Define a custom ModelAdmin class that includes configurations for the additional fields in your user model.
"""
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile
from django.utils.translation import gettext_lazy as _
class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'UserProfile'

class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline, )
    fieldsets = UserAdmin.fieldsets + (
        (_('User Profile'), {'fields': ('userprofile__role',)}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_role')

    def get_role(self, obj):
        return obj.userprofile.role
    get_role.short_description = 'Role'
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return []
        return super().get_inline_instances(request, obj)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
