from django.contrib import admin

from account.models import CustomUser
# Register your models here.
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username','usercolor','nickname']
    list_display_links = ['username','nickname']
