from djongo import models as mongo_models


# Model for ENY_NOW Data of Compere Power Meter
class EnyNowDataModelCPM(mongo_models.Model):
    _id = mongo_models.ObjectIdField()
    created_date = mongo_models.DateField(auto_now_add=True)
    created_time = mongo_models.TimeField(auto_now_add=True)
    device_code = mongo_models.CharField(max_length=360)
    topic = mongo_models.CharField(max_length=256)
    zygsz = mongo_models.FloatField()
    fygsz = mongo_models.FloatField()
    zwgsz = mongo_models.FloatField()
    fwgsz = mongo_models.FloatField()
    zyjsz = mongo_models.FloatField()
    fyjsz = mongo_models.FloatField()
    zyfsz = mongo_models.FloatField()
    fyfsz = mongo_models.FloatField()
    zypsz = mongo_models.FloatField()
    fypsz = mongo_models.FloatField()
    zyvsz = mongo_models.FloatField()
    fyvsz = mongo_models.FloatField()
    zydvsz = mongo_models.FloatField()
    fydvsz = mongo_models.FloatField()
    zy6sz = mongo_models.FloatField()
    fy6sz = mongo_models.FloatField()
    dmpmax = mongo_models.FloatField()
    dmpmaxoct = mongo_models.FloatField()
    dmsmax = mongo_models.FloatField()
    dmsmaxoct = mongo_models.FloatField() 
    uathd = mongo_models.FloatField()
    ubthd = mongo_models.FloatField()
    ucthd = mongo_models.FloatField()
    iathd = mongo_models.FloatField()
    ibthd = mongo_models.FloatField()
    icthd = mongo_models.FloatField()
    uaxbl3 = mongo_models.FloatField()
    ubxbl3 = mongo_models.FloatField()
    ucxbl3 = mongo_models.FloatField()
    iaxbl3 = mongo_models.FloatField()
    ibxbl3 = mongo_models.FloatField()
    icxbl3 = mongo_models.FloatField()
    uaxbl5 = mongo_models.FloatField()
    ubxbl5 = mongo_models.FloatField()
    ucxbl5 = mongo_models.FloatField()
    iaxbl5 = mongo_models.FloatField()
    ibxbl5 = mongo_models.FloatField()
    icxbl5 = mongo_models.FloatField()
    uaxbl7 = mongo_models.FloatField()
    ubxbl7 = mongo_models.FloatField()
    ucxbl7 = mongo_models.FloatField()
    iaxbl7 = mongo_models.FloatField()
    ibxbl7 = mongo_models.FloatField()
    icxbl7 = mongo_models.FloatField()
    iaxb3 = mongo_models.FloatField()
    ibxb3 = mongo_models.FloatField()
    icxb3 = mongo_models.FloatField()
    iaxb5 = mongo_models.FloatField()
    ibxb5 = mongo_models.FloatField()
    icxb5 = mongo_models.FloatField()
    iaxb7 = mongo_models.FloatField()
    ibxb7 = mongo_models.FloatField()
    icxb7 = mongo_models.FloatField()


    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.device_code
    

class TodayEnyNowDataModelCPM(mongo_models.Model):
    _id = mongo_models.ObjectIdField()
    created_date = mongo_models.DateField(auto_now_add=True)
    created_time = mongo_models.TimeField(auto_now_add=True)
    device_code = mongo_models.CharField(max_length=360)
    topic = mongo_models.CharField(max_length=256)
    zygsz = mongo_models.FloatField()

    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.device_code
    

class Last7DaysEnyNowDataModelCPM(mongo_models.Model):
    _id = mongo_models.ObjectIdField()
    created_date = mongo_models.DateField(auto_now_add=True)
    created_time = mongo_models.TimeField(auto_now_add=True)
    device_code = mongo_models.CharField(max_length=360)
    topic = mongo_models.CharField(max_length=256)
    zygsz = mongo_models.FloatField()

    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.device_code
    

class Last30DaysEnyNowDataModelCPM(mongo_models.Model):
    _id = mongo_models.ObjectIdField()
    created_date = mongo_models.DateField(auto_now_add=True)
    created_time = mongo_models.TimeField(auto_now_add=True)
    device_code = mongo_models.CharField(max_length=360)
    topic = mongo_models.CharField(max_length=256)
    zygsz = mongo_models.FloatField()

    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.device_code
    

class ThisYearEnyNowDataModelCPM(mongo_models.Model):
    _id = mongo_models.ObjectIdField()
    created_date = mongo_models.DateField(auto_now_add=True)
    created_time = mongo_models.TimeField(auto_now_add=True)
    device_code = mongo_models.CharField(max_length=360)
    topic = mongo_models.CharField(max_length=256)
    zygsz = mongo_models.FloatField()

    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.device_code