from os import system
from django.contrib import admin
from .models import Payment
# Register your models here.
class PaymentyAdmin(admin.ModelAdmin):
    list_display = ('system', 'date', 'recorder', 'amount')
    list_filter = (['recorder','system'])
admin.site.register(Payment,PaymentyAdmin)