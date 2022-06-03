from django.contrib import admin
from .models import Drink, Category

admin.site.register(Drink)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)
