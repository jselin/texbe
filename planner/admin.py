from django.contrib import admin

from .models import YarnManufacturer, Yarn, Plan

admin.site.register(YarnManufacturer)
admin.site.register(Yarn)
admin.site.register(Plan)

