from djongo import models as mongo_models


class ThermoHygrometerMongoModel(mongo_models.Model):
    _id = mongo_models.ObjectIdField()
    device_code = mongo_models.CharField(max_length=256)
    topic = mongo_models.CharField(max_length=256)
    created_date = mongo_models.DateField(auto_now_add=True)
    created_time = mongo_models.TimeField(auto_now_add=True)
    hum_p =  mongo_models.FloatField()
    temp_1_C = mongo_models.FloatField()
    dp_C =  mongo_models.FloatField()

    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.device_code


class TempThermoHygrometerMongoModel(mongo_models.Model):
    _id = mongo_models.ObjectIdField()
    device_code = mongo_models.CharField(max_length=256)
    topic = mongo_models.CharField(max_length=256)
    created_date = mongo_models.DateField(auto_now_add=True)
    created_time = mongo_models.TimeField(auto_now_add=True)
    hum_p =  mongo_models.FloatField()
    temp_1_C = mongo_models.FloatField()
    dp_C =  mongo_models.FloatField()

    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.device_code


class TodayThermoHygrometerMongoModel(mongo_models.Model):
    _id = mongo_models.ObjectIdField()
    device_code = mongo_models.CharField(max_length=256)
    topic = mongo_models.CharField(max_length=256)
    created_date = mongo_models.DateField(auto_now_add=True)
    created_time = mongo_models.TimeField(auto_now_add=True)
    hum_p =  mongo_models.FloatField()
    temp_1_C = mongo_models.FloatField()
    dp_C =  mongo_models.FloatField()

    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.device_code


class Last7DaysThermoHygrometerMongoModel(mongo_models.Model):
    _id = mongo_models.ObjectIdField()
    device_code = mongo_models.CharField(max_length=256)
    topic = mongo_models.CharField(max_length=256)
    created_date = mongo_models.DateField(auto_now_add=True)
    created_time = mongo_models.TimeField(auto_now_add=True)
    hum_p =  mongo_models.FloatField()
    temp_1_C = mongo_models.FloatField()
    dp_C =  mongo_models.FloatField()

    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.device_code


class Last30DaysThermoHygrometerMongoModel(mongo_models.Model):
    _id = mongo_models.ObjectIdField()
    device_code = mongo_models.CharField(max_length=256)
    topic = mongo_models.CharField(max_length=256)
    created_date = mongo_models.DateField(auto_now_add=True)
    created_time = mongo_models.TimeField(auto_now_add=True)
    hum_p =  mongo_models.FloatField()
    temp_1_C = mongo_models.FloatField()
    dp_C =  mongo_models.FloatField()

    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.device_code


class ThisYearThermoHygrometerMongoModel(mongo_models.Model):
    _id = mongo_models.ObjectIdField()
    device_code = mongo_models.CharField(max_length=256)
    topic = mongo_models.CharField(max_length=256)
    created_date = mongo_models.DateField(auto_now_add=True)
    created_time = mongo_models.TimeField(auto_now_add=True)
    hum_p =  mongo_models.FloatField()
    temp_1_C = mongo_models.FloatField()
    dp_C =  mongo_models.FloatField()

    class Meta:
        _use_db = 'nonrel'

    def __str__(self):
        return self.device_code

