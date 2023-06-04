from django.contrib import admin
from . models import suggestInfo, contactInfo

# Register your models here.

class InfoAdmin(admin.ModelAdmin):
    list_display = ('type','name','rating','description')

admin.site.register(suggestInfo,InfoAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')

admin.site.register(contactInfo, ContactAdmin)