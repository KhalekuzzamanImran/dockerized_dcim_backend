from base.serializers import DynamicFieldsModelSerializer
from pop.models import POP, POPDevice, POPDeviceState
from pop.CPM_RT_mongo_models import RTModelCPM, TemporaryRTModelCPM, TodayRTModelCPM, Last7DaysRTModelCPM, Last30DaysRTModelCPM, ThisYearRTModelCPM
from pop.CPM_ENY_NOW_mongo_models import EnyNowDataModelCPM, TemporaryEnyNowDataModelCPM, TodayEnyNowDataModelCPM, Last7DaysEnyNowDataModelCPM, Last30DaysEnyNowDataModelCPM, ThisYearEnyNowDataModelCPM
from pop.thermohygrometer_modhumati_models import ThermoHygrometerMongoModel, TempThermoHygrometerMongoModel, TodayThermoHygrometerMongoModel, Last7DaysThermoHygrometerMongoModel, Last30DaysThermoHygrometerMongoModel, ThisYearThermoHygrometerMongoModel
from pop.CCCL_generator_mongo_model import CCCLGenerator, TemporaryCCCLGenerator, TodayCCCLGenerator, Last7DaysCCCLGenerator, Last30DaysCCCLGenerator, ThisYearCCCLGenerator
from pop.CCCL_environment_mongo_model import CCCLEnvironment, TemporaryCCCLEnvironment, TodayCCCLEnvironment, Last7DaysCCCLEnvironment, Last30DaysCCCLEnvironment, ThisYearCCCLEnvironment
import datetime
import calendar

def get_date_range_this_week():
    today = datetime.date.today()
    start_of_week = today - datetime.timedelta(days=today.weekday() + 1)
    end_of_week = start_of_week + datetime.timedelta(days=6)
    return start_of_week, end_of_week


def get_date_range_this_month():
    today = datetime.date.today()
    _, last_day_of_month = calendar.monthrange(today.year, today.month)
    start_of_month = today.replace(day=1)
    end_of_month = today.replace(day=last_day_of_month)
    return start_of_month, end_of_month


def get_date_range_this_year():
    today = datetime.date.today()
    start_of_year = today.replace(month=1, day=1)
    end_of_year = today.replace(month=12, day=31)
    return start_of_year, end_of_year



class POPSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = POP
        fields = '__all__'


class POPDeviceSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = POPDevice
        fields = '__all__'


# Mongodb serializers
        
class RTModelCPMSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = RTModelCPM
        fields = '__all__'

        
class TemporaryRTModelCPMSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = TemporaryRTModelCPM
        fields = '__all__'


class TodayRTModelCPMSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = TodayRTModelCPM
        fields = '__all__'


class Last7DaysRTModelCPMSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Last7DaysRTModelCPM
        fields = '__all__'


class Last30DaysRTModelCPMSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Last30DaysRTModelCPM
        fields = '__all__'


class ThisYearRTModelCPMSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = ThisYearRTModelCPM
        fields = '__all__'


class EnyNowDataModelCPMSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = EnyNowDataModelCPM
        fields = '__all__'

class TemporaryEnyNowDataModelCPMSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = TemporaryEnyNowDataModelCPM
        fields = '__all__'


class TodayEnyNowDataModelCPMSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = TodayEnyNowDataModelCPM
        fields = '__all__'


class Last7DaysEnyNowDataModelCPMSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Last7DaysEnyNowDataModelCPM
        fields = '__all__'


class Last30DaysEnyNowDataModelCPMSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Last30DaysEnyNowDataModelCPM
        fields = '__all__'


class ThisYearEnyNowDataModelCPMSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = ThisYearEnyNowDataModelCPM
        fields = '__all__'


class ThermoHygrometerMongoModelSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = ThermoHygrometerMongoModel
        fields = '__all__'

class TempThermoHygrometerMongoModelSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = TempThermoHygrometerMongoModel
        fields = '__all__'


class TodayThermoHygrometerMongoModelSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = TodayThermoHygrometerMongoModel
        fields = '__all__'


class Last7DaysThermoHygrometerMongoModelSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Last7DaysThermoHygrometerMongoModel
        fields = '__all__'


class Last30DaysThermoHygrometerMongoModelSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Last30DaysThermoHygrometerMongoModel
        fields = '__all__'


class ThisYearThermoHygrometerMongoModelSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = ThisYearThermoHygrometerMongoModel
        fields = '__all__'


# CCCL Serializer
class CCCLGeneratorSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = CCCLGenerator
        fields = '__all__'

class TemporaryCCCLGeneratorSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = TemporaryCCCLGenerator
        fields = '__all__'


class TodayCCCLGeneratorSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = TodayCCCLGenerator
        fields = '__all__'


class Last7DaysCCCLGeneratorSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Last7DaysCCCLGenerator
        fields = '__all__'


class Last30DaysCCCLGeneratorSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Last30DaysCCCLGenerator
        fields = '__all__'


class ThisYearCCCLGeneratorSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = ThisYearCCCLGenerator
        fields = '__all__'


class CCCLEnvironmentSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = CCCLEnvironment
        fields = '__all__'

class TemporaryCCCLEnvironmentSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = TemporaryCCCLEnvironment
        fields = '__all__'


class TodayCCCLEnvironmentSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = TodayCCCLEnvironment
        fields = '__all__'


class Last7DaysCCCLEnvironmentSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Last7DaysCCCLEnvironment
        fields = '__all__'


class Last30DaysCCCLEnvironmentSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = Last30DaysCCCLEnvironment
        fields = '__all__'


class ThisYearCCCLEnvironmentSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = ThisYearCCCLEnvironment
        fields = '__all__'

# POP device state serializer
        

class POPDeviceStatesSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = POPDeviceState
        fields = '__all__'  # Include all fields by default


class LatestCCCLGeneratorDataSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = POPDeviceState
        exclude = ['data', 'created_at', 'updated_at']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            queryset = TodayCCCLGenerator.objects.all()
            data['latest'] = TodayCCCLGeneratorSerializer(queryset.last(), many=False).data
            # data['today'] = TodayRTModelCPMSerializer(queryset, many=True).data
            
        except:
            data = []

        return data
    

class LatestCCCLEnvironmentDataSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = POPDeviceState
        exclude = ['data', 'created_at', 'updated_at']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            queryset = TodayCCCLEnvironment.objects.all()
            data['latest'] = TodayCCCLEnvironmentSerializer(queryset.last(), many=False).data
            # data['today'] = TodayRTModelCPMSerializer(queryset, many=True).data
            
        except:
            data = []

        return data


class LatestRTDataSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = POPDeviceState
        exclude = ['data', 'created_at', 'updated_at']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            queryset = TodayRTModelCPM.objects.all()
            data['latest'] = TodayRTModelCPMSerializer(queryset.last(), many=False).data
            # data['today'] = TodayRTModelCPMSerializer(queryset, many=True).data
            
        except:
            data = []

        return data
    
        
class LatestThermohygrometerDataSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = POPDeviceState
        exclude = ['data', 'created_at', 'updated_at']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            queryset = TodayThermoHygrometerMongoModel.objects.all()
            data['latest'] = TodayThermoHygrometerMongoModelSerializer(queryset.last(), many=False).data
            # data['today'] = TodayThermoHygrometerMongoModelSerializer(queryset, many=True).data
            
        except:
            data = []

        return data
    

class LatestEnyNowDataSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = POPDeviceState
        exclude = ['data', 'created_at', 'updated_at']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            queryset = TodayEnyNowDataModelCPM.objects.all()
            data['latest'] = TodayEnyNowDataModelCPMSerializer(queryset.last(), many=False).data
            # data['today'] = TodayEnyNowDataModelCPMSerializer(queryset, many=True).data
            
        except:
            data = []

        return data
    

class CPMDataSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = POPDeviceState
        exclude = ['data', 'updated_at']

    def to_representation(self, instance):
        data = []

        if (instance.device_code.code == '3071523B00003'):
            if (instance.topic == 'MQTT_RT_DATA'):

                data = super().to_representation(instance)
                if instance.time_range == 'TODAY':

                    mongo_queryset = TodayRTModelCPM.objects.all()
                    data['latest'] = TodayRTModelCPMSerializer(mongo_queryset.last(), many=False).data
                    data['data'] = TodayRTModelCPMSerializer(mongo_queryset, many=True).data

                elif instance.time_range == 'LAST_7_DAYS':

                    mongo_queryset = Last7DaysRTModelCPM.objects.all()
                    data['latest'] = Last7DaysRTModelCPMSerializer(mongo_queryset.last(), many=False).data
                    data['data'] = Last7DaysRTModelCPMSerializer(mongo_queryset, many=True).data

                elif instance.time_range == 'LAST_30_DAYS':

                    mongo_queryset = Last30DaysRTModelCPM.objects.all()
                    data['latest'] = Last30DaysRTModelCPMSerializer(mongo_queryset.last(), many=False).data
                    data['data'] = Last30DaysRTModelCPMSerializer(mongo_queryset, many=True).data

                elif instance.time_range == 'THIS_YEAR': 
                    mongo_queryset = ThisYearRTModelCPM.objects.all()
                    data['latest'] = ThisYearRTModelCPMSerializer(mongo_queryset.last(), many=False).data
                    data['data'] = ThisYearRTModelCPMSerializer(mongo_queryset, many=True).data


        return data
    

class CCCLGeneratorSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = POPDeviceState
        exclude = ['data', 'updated_at']

    def to_representation(self, instance):
        data = []

        if (instance.device_code.code == 'GREEN_POWER_GENERATOR'):
            if (instance.topic == 'CCCL/PURBACHAL/ENM_01'):
                
                data = super().to_representation(instance)
                if instance.time_range == 'TODAY':
                    mongo_queryset = TodayCCCLGenerator.objects.all()
                    data['latest'] = TodayCCCLGeneratorSerializer(mongo_queryset.last(), many=False).data
                    data['data'] = TodayCCCLGeneratorSerializer(mongo_queryset, many=True).data

                elif instance.time_range == 'LAST_7_DAYS':

                    mongo_queryset = Last7DaysCCCLGenerator.objects.all()
                    data['latest'] = Last7DaysCCCLGeneratorSerializer(mongo_queryset.last(), many=False).data
                    data['data'] = Last7DaysCCCLGeneratorSerializer(mongo_queryset, many=True).data

                elif instance.time_range == 'LAST_30_DAYS':

                    mongo_queryset = Last30DaysCCCLGenerator.objects.all()
                    data['latest'] = Last30DaysCCCLGeneratorSerializer(mongo_queryset.last(), many=False).data
                    data['data'] = Last30DaysCCCLGeneratorSerializer(mongo_queryset, many=True).data

                elif instance.time_range == 'THIS_YEAR': 
                    mongo_queryset = TodayCCCLGenerator.objects.all()
                    data['latest'] = TodayCCCLGeneratorSerializer(mongo_queryset.last(), many=False).data
                    data['data'] = TodayCCCLGeneratorSerializer(mongo_queryset, many=True).data


        return data
    

class CCCLEnvironmentSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = POPDeviceState
        exclude = ['data', 'updated_at']

    def to_representation(self, instance):
        data = []

        if (instance.device_code.code == 'GREEN_POWER_THERMOHYGROMETER'):
            if (instance.topic == 'CCCL/PURBACHAL/ENV_01'):

                data = super().to_representation(instance)
                if instance.time_range == 'TODAY':

                    mongo_queryset = TodayCCCLEnvironment.objects.all()
                    data['latest'] = TodayCCCLEnvironmentSerializer(mongo_queryset.last(), many=False).data
                    data['data'] = TodayCCCLEnvironmentSerializer(mongo_queryset, many=True).data

                elif instance.time_range == 'LAST_7_DAYS':

                    mongo_queryset = Last7DaysCCCLEnvironment.objects.all()
                    data['latest'] = Last7DaysCCCLEnvironmentSerializer(mongo_queryset.last(), many=False).data
                    data['data'] = Last7DaysCCCLEnvironmentSerializer(mongo_queryset, many=True).data

                elif instance.time_range == 'LAST_30_DAYS':

                    mongo_queryset = Last30DaysCCCLEnvironment.objects.all()
                    data['latest'] = Last30DaysCCCLEnvironmentSerializer(mongo_queryset.last(), many=False).data
                    data['data'] = Last30DaysCCCLEnvironmentSerializer(mongo_queryset, many=True).data

                elif instance.time_range == 'THIS_YEAR': 
                    mongo_queryset = TodayCCCLEnvironment.objects.all()
                    data['latest'] = TodayCCCLEnvironmentSerializer(mongo_queryset.last(), many=False).data
                    data['data'] = TodayCCCLEnvironmentSerializer(mongo_queryset, many=True).data


        return data
    



class ThermohygrometerDataSerializer(DynamicFieldsModelSerializer):

    class Meta:
        model = POPDeviceState
        exclude = ['data', 'updated_at']

    def to_representation(self, instance):
        data = []

        if (instance.device_code.code == 'COLOCITY_THERMOHYGROMETER'):
            if (instance.topic == 'DCIM/COLOCITY/ENV_01'):

                data = super().to_representation(instance)
                if instance.time_range == 'TODAY':
                    mongo_queryset = TodayThermoHygrometerMongoModel.objects.all()
                    data['latest'] = TodayThermoHygrometerMongoModelSerializer(mongo_queryset.last(), many=False).data
                    data['data'] = TodayThermoHygrometerMongoModelSerializer(mongo_queryset, many=True).data

                if instance.time_range == 'LAST_7_DAYS':

                    mongo_queryset = Last7DaysThermoHygrometerMongoModel.objects.all()
                    data['latest'] = Last7DaysThermoHygrometerMongoModelSerializer(mongo_queryset.last(), many=False).data
                    data['data'] = Last7DaysThermoHygrometerMongoModelSerializer(mongo_queryset, many=True).data

                elif instance.time_range == 'LAST_30_DAYS':

                    mongo_queryset = Last30DaysThermoHygrometerMongoModel.objects.all()
                    data['latest'] = Last30DaysThermoHygrometerMongoModelSerializer(mongo_queryset.last(), many=False).data
                    data['data'] = Last30DaysThermoHygrometerMongoModelSerializer(mongo_queryset, many=True).data

                elif instance.time_range == 'THIS_YEAR': 
                    mongo_queryset = ThisYearThermoHygrometerMongoModel.objects.all()
                    data['latest'] = ThisYearThermoHygrometerMongoModelSerializer(mongo_queryset.last(), many=False).data
                    data['data'] = ThisYearThermoHygrometerMongoModelSerializer(mongo_queryset, many=True).data


        return data



# class DateWiseDataSerializer(DynamicFieldsModelSerializer):
#     class Meta:
#         model = PopDeviceState
#         exclude = ['data']

#     def to_representation(self, instance):

#         if (instance.device_code.code == '3071523B00003'):
#             if (instance.topic == 'MQTT_RT_DATA'):

#                 data = super().to_representation(instance)
#                 if instance.date == 'TODAY':
#                     mongo_queryset = TodayRTModelCPM.objects.all()
#                     data['data'] = TodayRTModelCPMSerializer(mongo_queryset, many=True).data

#                 elif instance.date == 'THIS_WEEK':
#                     start_of_week, end_of_week = get_date_range_this_week()
#                     mongo_queryset = ThisYearRTModelCPM.objects.filter(created_date__gte=start_of_week, created_date__lte=end_of_week)
#                     serialized_data = ThisMonthRTModelCPMSerializer(mongo_queryset, many=True).data
#                     data['data'] = serialized_data

#                 elif instance.date == 'THIS_MONTH': 
#                     start_of_month, end_of_month = get_date_range_this_month()
#                     mongo_queryset = ThisMonthRTModelCPM.objects.filter(created_date__gte=start_of_month, created_date__lte=end_of_month)
#                     data['data'] = ThisMonthRTModelCPMSerializer(mongo_queryset, many=True).data

#                 elif instance.date == 'THIS_YEAR': 
#                     mongo_queryset = ThisYearRTModelCPM.objects.all()
#                     data['data'] = ThisYearRTModelCPMSerializer(mongo_queryset, many=True).data

#                 return data
            


class MinuteLevelDataSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = POPDeviceState
        exclude = ['data']

    def to_representation(self, instance):
        data = []

        if (instance.device_code.code == '3071523B00003'):
            if (instance.topic == 'MQTT_ENY_NOW'):

                data = super().to_representation(instance)
                if instance.time_range == 'TODAY':

                    mongo_queryset = TodayEnyNowDataModelCPM.objects.all()
                    data['latest'] = TodayEnyNowDataModelCPMSerializer(mongo_queryset.last(), many=False).data
                    data['data'] = TodayEnyNowDataModelCPMSerializer(mongo_queryset, many=True).data

                elif instance.time_range == 'LAST_7_DAYS':
                    mongo_queryset = Last7DaysEnyNowDataModelCPM.objects.all()
                    data['latest'] = Last7DaysEnyNowDataModelCPMSerializer(mongo_queryset.last(), many=False).data
                    data['data'] = Last7DaysEnyNowDataModelCPMSerializer(mongo_queryset, many=True).data

                elif instance.time_range == 'LAST_30_DAYS':
                    mongo_queryset = Last30DaysEnyNowDataModelCPM.objects.all()
                    data['latest'] = Last30DaysEnyNowDataModelCPMSerializer(mongo_queryset.last(), many=False).data
                    data['data'] = Last30DaysEnyNowDataModelCPMSerializer(mongo_queryset, many=True).data

                elif instance.time_range == 'THIS_YEAR': 
                    mongo_queryset = ThisYearEnyNowDataModelCPM.objects.all()
                    data['latest'] = ThisYearEnyNowDataModelCPMSerializer(mongo_queryset.last(), many=False).data
                    data['data'] = ThisYearEnyNowDataModelCPMSerializer(mongo_queryset, many=True).data

        return data
