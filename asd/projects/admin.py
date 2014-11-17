from django.contrib import admin
from models import Project, ProjectType, Work, Procurance, Position, Employee

# Register your models here.
admin.site.register(Position)
admin.site.register(Employee)
admin.site.register(Work)
admin.site.register(ProjectType)
admin.site.register(Project)
admin.site.register(Procurance)
