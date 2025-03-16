from djongo import models
from rest_framework import serializers

class DataItem(models.Model):
    oid = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    class Meta:
        abstract = True  # Keep DataItem as abstract

class UpsModel(models.Model):
    _id = models.ObjectIdField(primary_key=True)
    timestamp = models.DateTimeField()
    data = models.JSONField()  # Use JSONField to store raw data

    objects = models.DjongoManager()

    class Meta:
        db_table = 'pop_upsdata'
        _use_db = 'nonrel'