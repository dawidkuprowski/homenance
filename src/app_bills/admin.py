from django.contrib import admin
from . import models

admin.site.register(models.Bill)
admin.site.register(models.BillType)
admin.site.register(models.Company)
admin.site.register(models.Currency)