from django.contrib import admin

from .models import MyBackground


@admin.register(MyBackground)
class MyBackgroundAdmin(admin.ModelAdmin):
    list_display = ["name"]
    list_display_links = ["name"]
    ordering = ["name"]
    search_fields = ["name"]
