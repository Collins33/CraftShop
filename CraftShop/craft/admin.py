from django.contrib import admin
from .models import categories,Craft

# Register your models here.
class CraftAdmin(admin.ModelAdmin):
    filter_horizontal=('category',)


admin.site.register(categories)
admin.site.register(Craft,CraftAdmin)
