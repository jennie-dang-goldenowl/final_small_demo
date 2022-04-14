from django.contrib import admin
from .models import Projects

class ProjectsModelAdmin(admin.ModelAdmin):
    # list_filter = ('dev')
    list_display = ('name', 'description', 'start_date', 'end_date', 'dev' )

admin.site.register(Projects, ProjectsModelAdmin)   