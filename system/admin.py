from django.contrib import admin
from .models import System
# Register your models here.

class SystemAdmin(admin.ModelAdmin):
    list_display = ('name', 'ram', 'graphic', 'cost_per_hour', 'is_busy')
    list_filter = (['ram', 'graphic', 'is_busy'])

admin.site.register(System,SystemAdmin)