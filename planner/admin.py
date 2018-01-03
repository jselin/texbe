from django.contrib import admin

from .models import Plan, YarnManufacturer, Yarn

# Register your models here.



class YarnAdmin(admin.ModelAdmin):
    list_display = ['name_text', 'manufacturer_name', 'material', 'thickness']

    def manufacturer_name(self, obj):
        return obj.manufacturer.name_text

admin.site.register(Plan)
admin.site.register(YarnManufacturer)
admin.site.register(Yarn, YarnAdmin)
