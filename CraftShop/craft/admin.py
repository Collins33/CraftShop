from django.contrib import admin
from .models import Category,Craft

# Register your models here.
# class CraftAdmin(admin.ModelAdmin):
#     filter_horizontal=('category',)


admin.site.register(Category)
admin.site.register(Craft)
