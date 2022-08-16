from django.contrib import admin

from.models import Weather, Provience, Town

# Register your models here.
admin.site.register(Weather)
admin.site.register(Provience)
admin.site.register(Town)
