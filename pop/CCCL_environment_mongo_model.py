from djongo import models as mongo_models

class CCCLEnvironment(mongo_models.Model):
    _id = mongo_models.ObjectIdField()
    created_date = mongo_models.DateField(auto_now_add=True)
    created_time = mongo_models.TimeField(auto_now_add=True)
    device_code = mongo_models.CharField(max_length=360)
    topic = mongo_models.CharField(max_length=256)
    pm1_0_ug_m3 = mongo_models.FloatField()
    pm2_5_ug_m3 = mongo_models.FloatField()
    pm10_0_ug_m3 = mongo_models.FloatField()
    hum_percent = mongo_models.FloatField()
    temp_1_c = mongo_models.FloatField()
    dp_c = mongo_models.FloatField()
    
    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.device_code
    
class TemporaryCCCLEnvironment(mongo_models.Model):
    _id = mongo_models.ObjectIdField()
    created_date = mongo_models.DateField(auto_now_add=True)
    created_time = mongo_models.TimeField(auto_now_add=True)
    device_code = mongo_models.CharField(max_length=360)
    topic = mongo_models.CharField(max_length=256)
    pm1_0_ug_m3 = mongo_models.FloatField()
    pm2_5_ug_m3 = mongo_models.FloatField()
    pm10_0_ug_m3 = mongo_models.FloatField()
    hum_percent = mongo_models.FloatField()
    temp_1_c = mongo_models.FloatField()
    dp_c = mongo_models.FloatField()
      
    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.device_code
    
class TodayCCCLEnvironment(mongo_models.Model):
    _id = mongo_models.ObjectIdField()
    created_date = mongo_models.DateField(auto_now_add=True)
    created_time = mongo_models.TimeField(auto_now_add=True)
    device_code = mongo_models.CharField(max_length=360)
    topic = mongo_models.CharField(max_length=256)
    pm1_0_ug_m3 = mongo_models.FloatField()
    pm2_5_ug_m3 = mongo_models.FloatField()
    pm10_0_ug_m3 = mongo_models.FloatField()
    hum_percent = mongo_models.FloatField()
    temp_1_c = mongo_models.FloatField()
    dp_c = mongo_models.FloatField()
      
    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.device_code
    
class Last7DaysCCCLEnvironment(mongo_models.Model):
    _id = mongo_models.ObjectIdField()
    created_date = mongo_models.DateField(auto_now_add=True)
    created_time = mongo_models.TimeField(auto_now_add=True)
    device_code = mongo_models.CharField(max_length=360)
    topic = mongo_models.CharField(max_length=256)
    pm1_0_ug_m3 = mongo_models.FloatField()
    pm2_5_ug_m3 = mongo_models.FloatField()
    pm10_0_ug_m3 = mongo_models.FloatField()
    hum_percent = mongo_models.FloatField()
    temp_1_c = mongo_models.FloatField()
    dp_c = mongo_models.FloatField()
      
    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.device_code
    
class Last30DaysCCCLEnvironment(mongo_models.Model):
    _id = mongo_models.ObjectIdField()
    created_date = mongo_models.DateField(auto_now_add=True)
    created_time = mongo_models.TimeField(auto_now_add=True)
    device_code = mongo_models.CharField(max_length=360)
    topic = mongo_models.CharField(max_length=256)
    pm1_0_ug_m3 = mongo_models.FloatField()
    pm2_5_ug_m3 = mongo_models.FloatField()
    pm10_0_ug_m3 = mongo_models.FloatField()
    hum_percent = mongo_models.FloatField()
    temp_1_c = mongo_models.FloatField()
    dp_c = mongo_models.FloatField()
      
    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.device_code
    
class ThisYearCCCLEnvironment(mongo_models.Model):
    _id = mongo_models.ObjectIdField()
    created_date = mongo_models.DateField(auto_now_add=True)
    created_time = mongo_models.TimeField(auto_now_add=True)
    device_code = mongo_models.CharField(max_length=360)
    topic = mongo_models.CharField(max_length=256)
    pm1_0_ug_m3 = mongo_models.FloatField()
    pm2_5_ug_m3 = mongo_models.FloatField()
    pm10_0_ug_m3 = mongo_models.FloatField()
    hum_percent = mongo_models.FloatField()
    temp_1_c = mongo_models.FloatField()
    dp_c = mongo_models.FloatField()
      
    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.device_code
  