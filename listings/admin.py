from django.contrib import admin
from .models import FallenSoldier, ArrestedPerson, MissingPerson

class FallenSoldierAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo')

class ArrestedPersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo')

class MissingPersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo')

admin.site.register(FallenSoldier, FallenSoldierAdmin)
admin.site.register(ArrestedPerson, ArrestedPersonAdmin)
admin.site.register(MissingPerson, MissingPersonAdmin)