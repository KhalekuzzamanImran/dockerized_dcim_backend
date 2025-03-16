from djongo import models as mongo_models
from pop.CCCL_environment_mongo_model import CCCLEnvironment, TemporaryCCCLEnvironment, TodayCCCLEnvironment, Last7DaysCCCLEnvironment, Last30DaysCCCLEnvironment, ThisYearCCCLEnvironment

import logging
logger = logging.getLogger(__name__)

def cccl_env_mongo_create(data, topic):
    
    # print(data)
    cccl_mongo = CCCLEnvironment.objects.create(

        device_code = data.get('id', '3071523B00003'),
        topic = topic,
        pm1_0_ug_m3 = data.get('pm1_0(ug/m3)', None),
        pm2_5_ug_m3 = data.get('pm2_5(ug/m3)', None),
        pm10_0_ug_m3 = data.get('pm10_0(ug/m3)', None),
        hum_percent = data.get('hum(%)', None),
        temp_1_c = data.get('temp_1(*C)', None),
        dp_c = data.get('dp(*C)', None),
    ) 

    logger.info(f"mongo_db = CCCLEnvironment, topic = {topic} created {cccl_mongo._id} succesfully")
    print('<!---------------------------Data successfully inserted in CCCLEnvironment------------------------------!>')

    temporary_cccl_mongo = TemporaryCCCLEnvironment.objects.create(

        device_code = data.get('id', '3071523B00003'),
        topic = topic,
        pm1_0_ug_m3 = data.get('pm1_0(ug/m3)', None),
        pm2_5_ug_m3 = data.get('pm2_5(ug/m3)', None),
        pm10_0_ug_m3 = data.get('pm10_0(ug/m3)', None),
        hum_percent = data.get('hum(%)', None),
        temp_1_c = data.get('temp_1(*C)', None),
        dp_c = data.get('dp(*C)', None),
    ) 

    logger.info(f"mongo_db = TemporaryCCCLEnvironment, topic = {topic} created {temporary_cccl_mongo._id} succesfully")
    print('<!---------------------------Data successfully inserted in TemporaryCCCLEnvironment------------------------------!>')

    today_cccl_mongo = TodayCCCLEnvironment.objects.create(

        device_code = data.get('id', '3071523B00003'),
        topic = topic,
        pm1_0_ug_m3 = data.get('pm1_0(ug/m3)', None),
        pm2_5_ug_m3 = data.get('pm2_5(ug/m3)', None),
        pm10_0_ug_m3 = data.get('pm10_0(ug/m3)', None),
        hum_percent = data.get('hum(%)', None),
        temp_1_c = data.get('temp_1(*C)', None),
        dp_c = data.get('dp(*C)', None),
    ) 

    logger.info(f"mongo_db = TodayCCCLEnvironment, topic = {topic} created {today_cccl_mongo._id} succesfully")
    print('<!---------------------------Data successfully inserted in TodayCCCLEnvironment------------------------------!>')


def date_wise_cccl_env_mongo_create(data, device_code, topic, flag):
    if 'LAST_7_DAYS' in flag:
        last7days_cccl_mongo = Last7DaysCCCLEnvironment.objects.create(
            device_code = device_code,
            topic = topic,
            pm1_0_ug_m3 = data.get('pm1_0_ug_m3', None),
            pm2_5_ug_m3 = data.get('pm2_5_ug_m3', None),
            pm10_0_ug_m3 = data.get('pm10_0_ug_m3', None),
            hum_percent = data.get('hum_percent', None),
            temp_1_c = data.get('temp_1_c', None),
            dp_c = data.get('dp_c', None),
        )

        logger.info(f"mongo_db = Last7DaysCCCLEnvironment, topic = {topic} created {last7days_cccl_mongo._id} succesfully")
        print('<!---------------------------Data successfully inserted in Last7DaysCCCLEnvironment------------------------------!>')
    
    if 'LAST_30_DAYS' in flag:
        last30days_cccl_mongo = Last30DaysCCCLEnvironment.objects.create(
            device_code = device_code,
            topic = topic,
            pm1_0_ug_m3 = data.get('pm1_0_ug_m3', None),
            pm2_5_ug_m3 = data.get('pm2_5_ug_m3', None),
            pm10_0_ug_m3 = data.get('pm10_0_ug_m3', None),
            hum_percent = data.get('hum_percent', None),
            temp_1_c = data.get('temp_1_c', None),
            dp_c = data.get('dp_c', None),
        )

        logger.info(f"mongo_db = Last30DaysCCCLEnvironment, topic = {topic} created {last30days_cccl_mongo._id} succesfully")
        print('<!---------------------------Data successfully inserted in Last30DaysCCCLEnvironment------------------------------!>')

    if "THIS_YEAR" in flag:
        thisyear_cccl_mongo = ThisYearCCCLEnvironment.objects.create(
            device_code = device_code,
            topic = topic,
            pm1_0_ug_m3 = data.get('pm1_0_ug_m3', None),
            pm2_5_ug_m3 = data.get('pm2_5_ug_m3', None),
            pm10_0_ug_m3 = data.get('pm10_0_ug_m3', None),
            hum_percent = data.get('hum_percent', None),
            temp_1_c = data.get('temp_1_c', None),
            dp_c = data.get('dp_c', None),
        )

        logger.info(f"mongo_db = ThisYearCCCLEnvironment, topic = {topic} created {thisyear_cccl_mongo._id} succesfully")
        print('<!---------------------------Data successfully inserted in ThisYearCCCLEnvironment------------------------------!>')


