from django.contrib import admin

# Register your models here.
# http://frontend.diffthink.kr/2018/12/book-4-django-admin.html
from dreams.models import DreamModel


@admin.register(DreamModel)
class DreamAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    # list_display_links = ['title','date_dream','created','read_cnt','color','contents']
    list_filter = ['author']
    search_fields = ['title']
# admin.site.register(DreamModel)