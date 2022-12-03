from django.contrib import admin
from .models import PlayTime
# Register your models here.

class PlayTimeAdmin(admin.ModelAdmin):
    list_display = ('pk','start_time', 'end_time')
    ordering = ('start_time','end_time')


admin.site.register(PlayTime, PlayTimeAdmin)


