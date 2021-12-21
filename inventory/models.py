from pathlib import Path
from pathlib import os
from os import name
from django.core.exceptions import MultipleObjectsReturned
from django.db import models
from django.db.models.fields.related import ForeignKey
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User

# Create your models here.

class MPTTMeta:
    order_insertion_by=['name']

class Category (models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    parent = models.ForeignKey(
        'self',
        related_name="children",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    def __str__(self):
        return self.name

class Tag (models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50)
    parent = models.ForeignKey(
        'self',
        related_name="children",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    def __str__(self):
        return self.name

class Storage_list (models.Model):  
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    parent = models.ForeignKey(
        'self',
        related_name="children",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    address=models.CharField(max_length=100)
    geo_tag=models.CharField(max_length=100)
    storage_photo=models.ImageField(upload_to='inventory/media/images/')
    keys_photo=models.ImageField(upload_to='inventory/media/images/')
    def __str__(self):
        return self.name


class Inventory (models.Model):
    creator = models.ForeignKey(
        User,
        related_name="inventories",
        on_delete=models.SET_NULL,
        null=True,
    )
    name = models.CharField(max_length=300)
    parent = models.ForeignKey(
        'self',
        related_name="children",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    status = models.CharField(max_length=300)
    create_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        Category,
        related_name="inventory",
        on_delete=models.SET_NULL,
        null=True,
    ) 
    tags=models.ManyToManyField(Tag,related_name="inventory")
    storage=models.ForeignKey(
        Storage_list,
        related_name="inventories",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    stellage = models.CharField(max_length=10)
    shelf = models.CharField(max_length=10)
    quality=models.PositiveSmallIntegerField(null=True,blank=False)
    units=models.CharField(max_length=10,null=True,blank=False)
    
    def __str__(self):
        return '%s %s' % (self.name,self.category)
    



class Images (models.Model):
    image = models.ImageField(upload_to='inventory/media/images/')
    Inventory=models.ForeignKey(
        Inventory,
        related_name="images",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    
