from pop.thermohygrometer_modhumati_models import (
    ThermoHygrometerMongoModel,
    TempThermoHygrometerMongoModel,
    TodayThermoHygrometerMongoModel,
    Last7DaysThermoHygrometerMongoModel,
    Last30DaysThermoHygrometerMongoModel,
    ThisYearThermoHygrometerMongoModel,
    ) 


import logging
logger = logging.getLogger(__name__)


def thermohygrometer_mongo_create(data, topic):

    thermohygrometer_mongo = ThermoHygrometerMongoModel.objects.create(
        device_code='ModhumatiBank-ENV_01',
        topic=topic, 
        hum_p=data.get('hum(%)', None),
        temp_1_C=data.get('temp_1(*C)', None),
        dp_C=data.get('dp(*C)', None),
    )
    
    print('<!---------------------------Data successfully inserted in ThermoHygrometerMongo------------------------------!>')
    # logger.info(f"ThermoHygrometerMongo {topic} data created succesfully")
    # print('thermohygrometer_mongo_created_id =', thermohygrometer_mongo._id)

    temp_thermohygrometer_mongo = TempThermoHygrometerMongoModel.objects.create(
        device_code='ModhumatiBank-ENV_01',
        topic=topic,
        hum_p=data.get('hum(%)', None),
        temp_1_C=data.get('temp_1(*C)', None),
        dp_C=data.get('dp(*C)', None),
    )
    
    print('<!---------------------------Data successfully inserted in TempThermoHygrometerMongoModel------------------------------!>')
    # logger.info(f"TempThermoHygrometerMongo {topic} data created {temp_thermohygrometer_mongo._id} succesfully")
    # print('temp_thermohygrometer_mongo_created_id =', temp_thermohygrometer_mongo._id)

    today_thermohygrometer_mongo = TodayThermoHygrometerMongoModel.objects.create(
        device_code='ModhumatiBank-ENV_01',
        topic=topic,
        hum_p=data.get('hum(%)', None),
        temp_1_C=data.get('temp_1(*C)', None),
        dp_C=data.get('dp(*C)', None),
    )
    
    print('<!---------------------------Data successfully inserted in TodayThermoHygrometerMongo------------------------------!>')
    # logger.info(f"TodayThermoHygrometerMongo {topic} data created {today_thermohygrometer_mongo._id} succesfully")
    # print('today_thermohygrometer_mongo_created_id =', today_thermohygrometer_mongo._id)



def date_wise_thermohygrometer_create(data, device_code, topic, flag):

    if not data.get('hum_p', None) and \
    not data.get('temp_1_C', None) and \
    not data.get('dp_C', None) :
        return ''  
    
    if 'LAST_7_DAYS' in flag:
        last7days_thermohygrometer_mongo = Last7DaysThermoHygrometerMongoModel.objects.create(
            device_code=device_code,
            topic=topic,
            hum_p=data.get('hum_p', None),
            temp_1_C=data.get('temp_1_C', None),
            dp_C=data.get('dp_C', None),
        )

        # number_of_rows = Last7DaysThermoHygrometerMongoModel.objects.all().count()

        # if(number_of_rows > 7):
        #     Last7DaysThermoHygrometerMongoModel.objects.filter(device_code=topic).order_by('-created_date').last().delete()

        logger.info(f"Last7DaysThermoHygrometerMongoModel {topic} data created {last7days_thermohygrometer_mongo._id} succesfully")
        print('<!---------------------------Data successfully inserted in Last7DaysThermoHygrometerMongoModel------------------------------!>')
    
    if 'LAST_30_DAYS' in flag:
        last30days_thermohygrometer_mongo = Last30DaysThermoHygrometerMongoModel.objects.create(
            device_code=device_code,
            topic=topic,
            hum_p=data.get('hum_p', None),
            temp_1_C=data.get('temp_1_C', None),
            dp_C=data.get('dp_C', None),
        )

        # number_of_rows = Last30DaysThermoHygrometerMongoModel.objects.all().count()
        # if(number_of_rows > 30):
        #     Last30DaysThermoHygrometerMongoModel.objects.filter(device_code=topic).order_by('-created_date').last().delete()

        logger.info(f"Last30DaysThermoHygrometerMongoModel {topic} data created {last30days_thermohygrometer_mongo._id} succesfully")
        print('<!---------------------------Data successfully inserted in Last30DaysThermoHygrometerMongoModel------------------------------!>')

    if 'THIS_YEAR' in flag:
        this_year_thermohygrometer_mongo = ThisYearThermoHygrometerMongoModel.objects.create(
            device_code=device_code,
            topic=topic,
            hum_p=data.get('hum_p', None),
            temp_1_C=data.get('temp_1_C', None),
            dp_C=data.get('dp_C', None),
        )

        # number_of_rows = ThisYearThermoHygrometerMongoModel.objects.all().count()
        # if(number_of_rows > 365):
        #     ThisYearThermoHygrometerMongoModel.objects.filter(device_code=topic).order_by('-created_date').last().delete()

        logger.info(f"ThisYearThermoHygrometerMongo {topic} data created {this_year_thermohygrometer_mongo._id} succesfully")
        print('<!---------------------------Data successfully inserted in ThisYearThermoHygrometerMongo------------------------------!>')

