from django.contrib import admin

from .models import *


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'salary', 'position')
    list_display_links = ('id', 'name', 'salary', 'position')


class ExcursionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date', 'term', 'price', 'employee')
    list_display_links = ('id', 'name', 'date', 'term', 'price', 'employee')


class HallAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'employee')
    list_display_links = ('id', 'name', 'employee')


class ExhibitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'author', 'material', 'hall')
    list_display_links = ('id', 'name', 'author', 'material', 'hall')


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Excursion, ExcursionAdmin)
admin.site.register(Hall, HallAdmin)
admin.site.register(Exhibit, ExhibitAdmin)
