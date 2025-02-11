import django
import os

from celery.schedules import crontab
from celery import Celery

from datetime import timedelta, datetime
from django.conf import settings
import json
import logging

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcim.settings')

logger = logging.getLogger(__name__)

app = Celery('dcim')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


# Created by Imran
# Timewise RT adn ENY_NOW and Thermohygrometer data created..
@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(minute=0, hour=0),
        delete_today_cpm_rt_and_enynow_data.s('all_rang'),
    )

    sender.add_periodic_task(
        crontab(minute='*/10'),
        prepare_last7days_rt_and_thermohygrometer_data.s('all_rang'),
    )

    sender.add_periodic_task(
        crontab(minute='*/30'),
        prepare_last30days_rt_enynow_and_thermohygrometer_data.s('all_rang'),
    )

    sender.add_periodic_task(
        crontab(minute=0, hour='*/6'),
        prepare_this_year_rt_enynow_and_thermohygrometer_data.s('all_rang'),
    )

    sender.add_periodic_task(
        crontab(minute=0, hour='*/6'),
        prepare_this_year_rt_enynow_and_thermohygrometer_data.s('all_rang'),
    )



def prepare_rt_data(data):
    import numpy as np

    item = {
        'ua': 0,
        'ub': 0,
        'uc': 0,
        'ia': 0,
        'ib': 0,
        'ic': 0,
        # 'uab': 0,
        # 'ubc': 0,
        # 'uca': 0,
        'pa': 0,
        'pb': 0,
        'pc': 0,
        'zyggl': 0,
        # 'qa': 0,
        # 'qb': 0,
        # 'qc': 0,
        # 'zwggl': 0,
        # 'sa': 0,
        # 'sb': 0,
        # 'sc': 0,
        # 'zszgl': 0,
        'pfa': 0,
        'pfb': 0,
        'pfc': 0,
        'zglys': 0,
        'f': 0,
        # 'u0': 0,
        # 'u_plus': 0,
        # 'u_minus': 0,
        # 'i0': 0,
        # 'i_plus': 0,
        # 'i_minus': 0,
        # 'uxja': 0,
        # 'uxjb': 0,
        # 'uxjc': 0,
        # 'ixja': 0,
        # 'ixjb': 0,
        # 'ixjc': 0,
        # 'unb': 0,
        # 'inb': 0,
        'pdm': 0,
        'qdm': 0,
        'sdm': 0,
    }

    statistics = {}
    # Loop through each variable and calculate statistics
    for variable in item.keys():  # Assuming all data points have the same keys
        values = []
        for entry in data:
            if entry.get(variable) is not None:
                values.append(entry.get(variable))
        statistics[variable] = np.mean(values) if len(values) > 0 else None
    return statistics


def prepare_enynow_data(data):
    import numpy as np

    item = {
        'zygsz': 0,
    }

    statistics = {}
    # Loop through each variable and calculate statistics
    for variable in item.keys():  # Assuming all data points have the same keys
        values = []
        for entry in data:
            if entry.get(variable) is not None:
                values.append(entry.get(variable))
        statistics[variable] = np.mean(values) if len(values) > 0 else None
    return statistics

def prepare_thermohygrometer_data(data):
    import numpy as np

    item = {
      "hum_p": 0,
      "temp_1_C": 0,
      "dp_C": 0
    }

    statistics = {}
    # Loop through each variable and calculate statistics
    for variable in item.keys():  # Assuming all data points have the same keys
        values = []
        for entry in data:
            if entry.get(variable) is not None:
                values.append(entry.get(variable))
        statistics[variable] = np.mean(values) if len(values) > 0 else None
    return statistics


@app.task
def delete_today_cpm_rt_and_enynow_data(arg):
    from pop.CPM_RT_mongo_models import TodayRTModelCPM
    from pop.CPM_ENY_NOW_mongo_models import TodayEnyNowDataModelCPM
    from pop.thermohygrometer_modhumati_models import TodayThermoHygrometerMongoModel

    today_cpm_rt_data_queryset = TodayRTModelCPM.objects.all()
    today_cpm_rt_data_queryset.delete()
    logger.warning(f"TodayRTModelCPM data deleted succesfully")

    today_cpm_enynow_data_queryset = TodayEnyNowDataModelCPM.objects.all()
    today_cpm_enynow_data_queryset.delete()
    logger.warning(f"TodayEnyNowDataModelCPM data deleted succesfully")

    today_thermohygrometer_data_queryset = TodayThermoHygrometerMongoModel.objects.all()
    today_thermohygrometer_data_queryset.delete()
    logger.warning(f"TodayThermoHygrometerMongoModel data deleted succesfully")

  

@app.task
def prepare_last7days_rt_and_thermohygrometer_data(arg):
    from pop.CPM_RT_mongo_models import TemporaryRTModelCPM
    from pop.api.serializers import TemporaryRTModelCPMSerializer
    from pop.CPM_RT_mixins import date_wise_cpm_rt_mongo_create

    from pop.thermohygrometer_modhumati_models import TempThermoHygrometerMongoModel
    from pop.api.serializers import TempThermoHygrometerMongoModelSerializer
    from pop.thermohygrometer_modhumati_mixins import date_wise_thermohygrometer_create

    from pop.models import POPDeviceState, POP, POPDevice

    for pop in POP.objects.filter(is_active=True):
        for device in POPDevice.objects.filter(pop_name=pop.id):
            for state in POPDeviceState.objects.filter(device_code=device.id):

                if state.time_range == 'TODAY':
                    if state.topic == 'MQTT_RT_DATA':
                        temp_rt_mongo_cpm_queryset = TemporaryRTModelCPM.objects.all()
                        data = TemporaryRTModelCPMSerializer(temp_rt_mongo_cpm_queryset, many=True).data
                        date_wise_cpm_rt_mongo_create(prepare_rt_data(data), state.device_code, state.topic, ['LAST_7_DAYS'])
                        temp_rt_mongo_cpm_queryset.delete()
                        logger.warning(f"TemporaryRTModelCPM {state.topic} data deleted succesfully")

                    if state.topic == 'DCIM/ModhumatiBank/ENV_01':
                        temp_thermohygro_mongo_queryset = TempThermoHygrometerMongoModel.objects.all()
                        data = TempThermoHygrometerMongoModelSerializer(temp_thermohygro_mongo_queryset, many=True).data
                        date_wise_thermohygrometer_create(prepare_thermohygrometer_data(data), state.device_code, state.topic, ['LAST_7_DAYS'])
                        temp_thermohygro_mongo_queryset.delete()
                        logger.warning(f"TempThermoHygrometerMongoModel {state.topic} data deleted succesfully")


@app.task
def prepare_last30days_rt_enynow_and_thermohygrometer_data(arg):
    from pop.CPM_RT_mongo_models import Last7DaysRTModelCPM
    from pop.api.serializers import Last7DaysRTModelCPMSerializer
    from pop.CPM_RT_mixins import date_wise_cpm_rt_mongo_create
    from pop.CPM_ENY_NOW_mongo_models import Last7DaysEnyNowDataModelCPM
    from pop.api.serializers import Last7DaysEnyNowDataModelCPMSerializer
    from pop.CPM_ENY_NOW_mongo_mixins import date_wise_cpm_enynow_mongo_create
    from pop.thermohygrometer_modhumati_models import Last7DaysThermoHygrometerMongoModel
    from pop.api.serializers import Last7DaysThermoHygrometerMongoModelSerializer
    from pop.thermohygrometer_modhumati_mixins import date_wise_thermohygrometer_create
    
    from pop.models import POPDeviceState, POP, POPDevice

    for pop in POP.objects.filter(is_active=True):
        for device in POPDevice.objects.filter(pop_name=pop.id):
            # print(device)
            for state in POPDeviceState.objects.filter(device_code=device.id):
                # print(state.id)
                # print(state.device_code.code)
                # print(state)

                if state.device_code.code  == '3071523B00003':
                    # print(state.device_code)
                    if state.time_range == 'LAST_7_DAYS':
                        # print(state.time_range)
                        if(state.topic == 'MQTT_RT_DATA'):
                            # print(state.topic)
                            last7days_rt_mongo_cpm_queryset = Last7DaysRTModelCPM.objects.order_by('-created_date', '-created_time')[:3]
                            data = Last7DaysRTModelCPMSerializer(last7days_rt_mongo_cpm_queryset, many=True).data
                            date_wise_cpm_rt_mongo_create(prepare_rt_data(data), state.device_code, state.topic, ['LAST_30_DAYS'])
                            # temp_rt_mongo_cpm_queryset.delete()
                            # logger.warning(f"TemporaryRTModelCPM {state.topic} data deleted succesfully")

                        if state.topic == 'MQTT_ENY_NOW':
                            last7days_enynow_mongo_cpm_queryset = Last7DaysEnyNowDataModelCPM.objects.order_by('-created_date', '-created_time')[:2]
                            data = Last7DaysEnyNowDataModelCPMSerializer(last7days_enynow_mongo_cpm_queryset, many=True).data
                            date_wise_cpm_enynow_mongo_create(prepare_enynow_data(data), state.device_code, state.topic, ['LAST_30_DAYS'])
                            # temp_rt_mongo_cpm_queryset.delete()
                            # logger.warning(f"TemporaryRTModelCPM {state.topic} data deleted succesfully")

                        if state.topic == 'MQTT_ENY_NOW':
                            last7days_enynow_mongo_cpm_queryset = Last7DaysEnyNowDataModelCPM.objects.order_by('-created_date', '-created_time')[:2]
                            data = Last7DaysEnyNowDataModelCPMSerializer(last7days_enynow_mongo_cpm_queryset, many=True).data
                            date_wise_cpm_enynow_mongo_create(prepare_enynow_data(data), state.device_code, state.topic, ['LAST_30_DAYS'])
                            # temp_rt_mongo_cpm_queryset.delete()
                            # logger.warning(f"TemporaryRTModelCPM {state.topic} data deleted succesfully")


                        if(state.topic == 'DCIM/ModhumatiBank/ENV_01'):
                            # print(state.topic)
                            last7days_thermohygrometer_queryset = Last7DaysThermoHygrometerMongoModel.objects.order_by('-created_date', '-created_time')[:3]
                            data = Last7DaysThermoHygrometerMongoModelSerializer(last7days_thermohygrometer_queryset, many=True).data
                            date_wise_thermohygrometer_create(prepare_thermohygrometer_data(data), state.device_code, state.topic, ['LAST_30_DAYS'])
                            # temp_rt_mongo_cpm_queryset.delete()
                            # logger.warning(f"TemporaryRTModelCPM {state.topic} data deleted succesfully")
                    


@app.task
def prepare_this_year_rt_enynow_and_thermohygrometer_data(arg):
    from pop.CPM_RT_mongo_models import Last30DaysRTModelCPM
    from pop.api.serializers import Last30DaysRTModelCPMSerializer
    from pop.CPM_RT_mixins import date_wise_cpm_rt_mongo_create
    from pop.CPM_ENY_NOW_mongo_models import Last30DaysEnyNowDataModelCPM
    from pop.api.serializers import Last30DaysEnyNowDataModelCPMSerializer
    from pop.CPM_ENY_NOW_mongo_mixins import date_wise_cpm_enynow_mongo_create
    from pop.thermohygrometer_modhumati_models import Last30DaysThermoHygrometerMongoModel
    from pop.api.serializers import Last30DaysThermoHygrometerMongoModelSerializer
    from pop.thermohygrometer_modhumati_mixins import date_wise_thermohygrometer_create

    from pop.models import POPDeviceState, POP, POPDevice

    for pop in POP.objects.filter(is_active=True):
        for device in POPDevice.objects.filter(pop_name=pop.id):
            # print(device)
            for state in POPDeviceState.objects.filter(device_code=device.id):
                # print(state.id)
                # print(state.device_code.code)
                # print(state)

                if state.device_code.code  == '3071523B00003':
                    # print(state.device_code)
                    if state.time_range == 'LAST_30_DAYS':
                        # print(state.date)
                        if(state.topic == 'MQTT_RT_DATA'):
                            # print(state.topic)
                            last30days_rt_mongo_cpm_queryset = Last30DaysRTModelCPM.objects.order_by('-created_date', '-created_time')[:12]
                            data = Last30DaysRTModelCPMSerializer(last30days_rt_mongo_cpm_queryset, many=True).data
                            date_wise_cpm_rt_mongo_create(prepare_rt_data(data), state.device_code, state.topic, ['THIS_YEAR'])
                            # temp_rt_mongo_cpm_queryset.delete()
                            # logger.warning(f"TemporaryRTModelCPM {state.topic} data deleted succesfully")

                        if state.topic == 'MQTT_ENY_NOW':
                            last30days_enynow_mongo_cpm_queryset = Last30DaysEnyNowDataModelCPM.objects.order_by('-created_date', '-created_time')[:12]
                            data = Last30DaysEnyNowDataModelCPMSerializer(last30days_enynow_mongo_cpm_queryset, many=True).data
                            date_wise_cpm_enynow_mongo_create(prepare_enynow_data(data), state.device_code, state.topic, ['THIS_YEAR'])
                            # temp_rt_mongo_cpm_queryset.delete()
                            # logger.warning(f"TemporaryRTModelCPM {state.topic} data deleted succesfully")

            
                        if(state.topic == 'DCIM/ModhumatiBank/ENV_01'):
                            # print(state.topic)
                            last30days_thermohygrometer_queryset = Last30DaysThermoHygrometerMongoModel.objects.order_by('-created_date', '-created_time')[:12]
                            data = Last30DaysThermoHygrometerMongoModelSerializer(last30days_thermohygrometer_queryset, many=True).data
                            date_wise_thermohygrometer_create(prepare_thermohygrometer_data(data), state.device_code, state.topic, ['THIS_YEAR'])
                            # temp_rt_mongo_cpm_queryset.delete()
                            # logger.warning(f"TemporaryRTModelCPM {state.topic} data deleted succesfully")
 
