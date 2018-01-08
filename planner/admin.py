from django.contrib import admin

from .models import YarnManufacturer, YarnNumberingSystem, Yarn, Plan

admin.site.register(YarnNumberingSystem)
admin.site.register(YarnManufacturer)
admin.site.register(Yarn)
admin.site.register(Plan)

