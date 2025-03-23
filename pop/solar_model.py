from djongo import models

class CurrentData(models.Model):
    values = models.JSONField()  # Stores list of float values
    class Meta:
        abstract = True  # Prevents table creation

class PowerData(models.Model):
    values = models.JSONField()  # Stores list of float values
    class Meta:
        abstract = True

class EnergyConsumption(models.Model):
    values = models.JSONField()  # Stores list of int values
    class Meta:
        abstract = True

class SolarReading(models.Model):
    _id = models.ObjectIdField()
    timestamp = models.DateTimeField()
    current = models.EmbeddedField(
        model_container=CurrentData
    )
    power = models.EmbeddedField(
        model_container=PowerData
    )
    energy_consumption = models.EmbeddedField(
        model_container=EnergyConsumption
    )

    objects = models.DjongoManager()

    class Meta:
        db_table = 'pop_solar_readings'
        _use_db = 'nonrel'
