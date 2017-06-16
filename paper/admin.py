from django.contrib import admin

from .models import Column,Paper


class ColumnAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'intro', 'nav_display', 'home_display')

class PaperAdmin(admin.ModelAdmin):
    list_display = ('column', 'title', 'slug', 'author', 'file')


admin.site.register(Column, ColumnAdmin)
admin.site.register(Paper, PaperAdmin)
