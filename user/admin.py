from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_type', 'is_active', 'is_staff')
    list_filter = ('user_type', 'is_active', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('user_type',)

    fieldsets = (
        (None, {
            'fields': ('username', 'password', 'email')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'phone_no', 'terms_agree', 'remember_me')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('User Type', {
            'fields': ('user_type',)
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)

