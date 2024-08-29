from djongo import models as mongo_models

# Model for ENY_FRZ Data of Compere Power Meter
class EnyFrzDataModelCPM(mongo_models.Model):
    _id = mongo_models.ObjectIdField()
    created_date = mongo_models.DateField(auto_now_add=True)
    created_time = mongo_models.TimeField(auto_now_add=True)
    device_code = mongo_models.CharField(max_length=360)
    topic = mongo_models.CharField(max_length=256)
    zydvdd = mongo_models.FloatField(default=0.0)
    fydvdd = mongo_models.FloatField(default=0.0)
    zy6dd = mongo_models.FloatField(default=0.0)
    fy6dd = mongo_models.FloatField(default=0.0)
    mfhl = mongo_models.FloatField(default=0.0)

    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.device_code