from django.contrib import admin

# Register your models here.
from django.contrib import admin
from projects.models import Project, Task

# Registering the models with the admin site
admin.site.register(Project)
admin.site.register(Task)
