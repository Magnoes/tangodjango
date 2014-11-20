from django.contrib import admin
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')
    search_fields = ['title']
    list_filter = ['category']

admin.site.register(Category)
admin.site.register(Page, PageAdmin)
