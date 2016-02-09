from django.contrib import admin
from .models import PersonalComputer, License
from django.contrib.auth.models import Group

admin.site.unregister(Group)

admin.site.register(PersonalComputer)

class LicenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'pc')

admin.site.register(License, LicenseAdmin)
