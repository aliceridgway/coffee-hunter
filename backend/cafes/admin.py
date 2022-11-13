from django.contrib import admin

from . import models

# Register your models here.

admin.site.register(models.Cafe)
admin.site.register(models.Review)
admin.site.register(models.Tag)
