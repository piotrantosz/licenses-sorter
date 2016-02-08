from django.contrib import admin

from .models import PersonalComputer, License

admin.site.register(PersonalComputer)
admin.site.register(License)
