from django.contrib import admin
from .models import FallenSoldier, ArrestedPerson, MissingPerson

admin.site.register(FallenSoldier)
admin.site.register(ArrestedPerson)
admin.site.register(MissingPerson)