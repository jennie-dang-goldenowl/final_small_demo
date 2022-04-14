from django.contrib import admin
from .models import Dev

class DevModelAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'description' )

admin.site.register(Dev, DevModelAdmin)  