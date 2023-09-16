from django.contrib import admin
from .models import *

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "category",)
    list_display_links = ('id', 'first_name')
    list_filter = ("category", "birthday",)
    search_fields = ("first_name__startswith",)
    

@admin.register(PersonCategory)
class PersonCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name__startswith",)