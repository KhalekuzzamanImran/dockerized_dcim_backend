from djongo import models as mongo_models

class CCCLGenerator(mongo_models.Model):
    _id = mongo_models.ObjectIdField()
    created_date = mongo_models.DateField(auto_now_add=True)
    created_time = mongo_models.TimeField(auto_now_add=True)
    device_code = mongo_models.CharField(max_length=360)
    topic = mongo_models.CharField(max_length=256)
    ua = mongo_models.FloatField()
    ub = mongo_models.FloatField()
    uc = mongo_models.FloatField()
    ia = mongo_models.FloatField()
    ib = mongo_models.FloatField()
    ic = mongo_models.FloatField()
    pa = mongo_models.FloatField()
    pb = mongo_models.FloatField()
    pc = mongo_models.FloatField()
    zyggl = mongo_models.FloatField()
    pfa = mongo_models.FloatField()
    pfb = mongo_models.FloatField()
    pfc = mongo_models.FloatField()
    zglys = mongo_models.FloatField()
    f = mongo_models.FloatField()
    zygsz = mongo_models.FloatField()
      
    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.device_code
    
    
class TodayCCCLGenerator(mongo_models.Model):
    _id = mongo_models.ObjectIdField()
    created_date = mongo_models.DateField(auto_now_add=True)
    created_time = mongo_models.TimeField(auto_now_add=True)
    device_code = mongo_models.CharField(max_length=360)
    topic = mongo_models.CharField(max_length=256)
    ua = mongo_models.FloatField()
    ub = mongo_models.FloatField()
    uc = mongo_models.FloatField()
    ia = mongo_models.FloatField()
    ib = mongo_models.FloatField()
    ic = mongo_models.FloatField()
    pa = mongo_models.FloatField()
    pb = mongo_models.FloatField()
    pc = mongo_models.FloatField()
    zyggl = mongo_models.FloatField()
    pfa = mongo_models.FloatField()
    pfb = mongo_models.FloatField()
    pfc = mongo_models.FloatField()
    zglys = mongo_models.FloatField()
    f = mongo_models.FloatField()
    zygsz = mongo_models.FloatField()
      
    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.device_code
    
class Last7DaysCCCLGenerator(mongo_models.Model):
    _id = mongo_models.ObjectIdField()
    created_date = mongo_models.DateField(auto_now_add=True)
    created_time = mongo_models.TimeField(auto_now_add=True)
    device_code = mongo_models.CharField(max_length=360)
    topic = mongo_models.CharField(max_length=256)
    ua = mongo_models.FloatField()
    ub = mongo_models.FloatField()
    uc = mongo_models.FloatField()
    ia = mongo_models.FloatField()
    ib = mongo_models.FloatField()
    ic = mongo_models.FloatField()
    pa = mongo_models.FloatField()
    pb = mongo_models.FloatField()
    pc = mongo_models.FloatField()
    zyggl = mongo_models.FloatField()
    pfa = mongo_models.FloatField()
    pfb = mongo_models.FloatField()
    pfc = mongo_models.FloatField()
    zglys = mongo_models.FloatField()
    f = mongo_models.FloatField()
    zygsz = mongo_models.FloatField()
      
    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.device_code
    
class Last30DaysCCCLGenerator(mongo_models.Model):
    _id = mongo_models.ObjectIdField()
    created_date = mongo_models.DateField(auto_now_add=True)
    created_time = mongo_models.TimeField(auto_now_add=True)
    device_code = mongo_models.CharField(max_length=360)
    topic = mongo_models.CharField(max_length=256)
    ua = mongo_models.FloatField()
    ub = mongo_models.FloatField()
    uc = mongo_models.FloatField()
    ia = mongo_models.FloatField()
    ib = mongo_models.FloatField()
    ic = mongo_models.FloatField()
    pa = mongo_models.FloatField()
    pb = mongo_models.FloatField()
    pc = mongo_models.FloatField()
    zyggl = mongo_models.FloatField()
    pfa = mongo_models.FloatField()
    pfb = mongo_models.FloatField()
    pfc = mongo_models.FloatField()
    zglys = mongo_models.FloatField()
    f = mongo_models.FloatField()
    zygsz = mongo_models.FloatField()
      
    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.device_code
    
class ThisYearCCCLGenerator(mongo_models.Model):
    _id = mongo_models.ObjectIdField()
    created_date = mongo_models.DateField(auto_now_add=True)
    created_time = mongo_models.TimeField(auto_now_add=True)
    device_code = mongo_models.CharField(max_length=360)
    topic = mongo_models.CharField(max_length=256)
    ua = mongo_models.FloatField()
    ub = mongo_models.FloatField()
    uc = mongo_models.FloatField()
    ia = mongo_models.FloatField()
    ib = mongo_models.FloatField()
    ic = mongo_models.FloatField()
    pa = mongo_models.FloatField()
    pb = mongo_models.FloatField()
    pc = mongo_models.FloatField()
    zyggl = mongo_models.FloatField()
    pfa = mongo_models.FloatField()
    pfb = mongo_models.FloatField()
    pfc = mongo_models.FloatField()
    zglys = mongo_models.FloatField()
    f = mongo_models.FloatField()
    zygsz = mongo_models.FloatField()
      
    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.device_code
  