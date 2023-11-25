from django.db import models
from django.contrib.auth.models import User

from datetime import datetime

# Create your models here.
class Currency(models.Model):
    SIDES = (
        (-1, 'Lewo'),
        (1, 'Prawo')
    )
    
    name = models.CharField(max_length=32)
    tag = models.CharField(max_length=8)
    side = models.IntegerField(choices=SIDES)

    def __str__(self):
        return self.name

class Company(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name

class BillType(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.name

class Bill(models.Model):
    type = models.ForeignKey(BillType, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    amount = models.DecimalField(decimal_places=2, max_digits=16)
    comment = models.TextField(max_length=256, null=True, blank=True)

    author = models.ForeignKey(User, on_delete=models.PROTECT)

    created_on = models.DateTimeField(default=datetime.now(), blank=True)
    changed_on = models.DateTimeField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.id