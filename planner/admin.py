from django.contrib import admin

from .models import YarnManufacturer, YarnNumberingSystem, Yarn

# Register your models here.
class YarnAdmin(admin.ModelAdmin):
    list_display = ['name', 'manufacturer', 'material', 'number', 'numbering_system', 'sett', 'sett_unit']

    def manufacturer(self, obj):
        return obj.manufacturer.name_text

    def sett_unit(self, obj):
        return obj.sett.name

admin.site.register(YarnNumberingSystem)
admin.site.register(YarnManufacturer)
admin.site.register(Yarn, YarnAdmin)
