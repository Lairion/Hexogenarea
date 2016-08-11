from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ListMaster(models.Model):
    SIZE_AREA = (("small","small"),("middle","middle"),("large","large"))
    name_area = models.CharField(max_length=100)
    type_area = models.CharField(choices=SIZE_AREA)
    date_area = models.DateTimeField(auto_now=true,auto_now_add=true)
