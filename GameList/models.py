from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ListMaster(models.Model):
    SIZE_AREA = (("small","small"),("middle","middle"),("large","large"))
    STATUS = (("Active","Active"),("Pause","Pause"),("Finished","Finished"))
    name_area = models.CharField(max_length=100)
    type_area = models.CharField(max_length=7,choices=SIZE_AREA)
    name_master = models.CharField(max_length=100)
    status = models.CharField(max_length=7,choices=STATUS)
    date_area = models.DateTimeField(auto_now=True,auto_now_add=False)
    
    def __str__(self):
        return str(self.name_area)
