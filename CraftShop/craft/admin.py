from django.contrib import admin
from .models import Artist,categories,Craft

# Register your models here.

admin.site.register(Artist)
admin.site.register(categories)
admin.site.register(Craft)
