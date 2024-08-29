from djongo import models as mongo_models

# Model for Day Data of Compere Power Meter
class DayDataModelCPM(mongo_models.Model):
    _id = mongo_models.ObjectIdField()
    created_date = mongo_models.DateField(auto_now_add=True)
    created_time = mongo_models.TimeField(auto_now_add=True)
    device_code = mongo_models.CharField(max_length=360)
    topic = mongo_models.CharField(max_length=256)
    zydvsz = mongo_models.FloatField()
    fydvsz = mongo_models.FloatField()
    zy6sz = mongo_models.FloatField()
    fy6sz = mongo_models.FloatField()

    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.device_code