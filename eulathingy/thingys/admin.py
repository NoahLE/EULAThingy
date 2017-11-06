from django.contrib import admin

from .models import ThingyDoc, ThingyString

# Register your models here.
admin.site.register(ThingyDoc)
admin.site.register(ThingyString)
