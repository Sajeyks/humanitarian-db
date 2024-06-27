from django.contrib import admin
from .models import FallenSoldier, ArrestedPerson, MissingPerson

class FallenSoldierAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag')
    readonly_fields = ['image_tag']

class ArrestedPersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag')
    readonly_fields = ['image_tag']

class MissingPersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_tag')
    readonly_fields = ['image_tag']

admin.site.register(FallenSoldier, FallenSoldierAdmin)
admin.site.register(ArrestedPerson, ArrestedPersonAdmin)
admin.site.register(MissingPerson, MissingPersonAdmin)#4a8acf