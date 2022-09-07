from django.contrib import admin
from .models import CustomUser


# Register your models here.
@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):

    list_display = ['user_uuid', 'email', 'name', 'created_at', 'updated_at']
    ordering = ('-updated_at',)
    search_fields = ['email', 'name', 'gender']
    list_filter = ['is_superuser', 'is_staff', 'is_active']
    fieldsets = (
        (None, {"fields": ('email', 'password', 'name')}),
        ('Personal', {"fields": ('phone', 'gender')}),
        ('Permission', {"fields": ('is_superuser', 'is_staff',
         'is_active', 'groups', 'user_permissions')}),
    )
