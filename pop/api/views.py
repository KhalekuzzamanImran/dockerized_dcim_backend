from rest_framework import viewsets, filters, status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend

from pop.api.serializers import (
    POPSerializer, POPDeviceSerializer, POPDeviceStatesSerializer,
    LatestRTDataSerializer, LatestEnyNowDataSerializer, LatestThermohygrometerDataSerializer,
    CPMDataSerializer, MinuteLevelDataSerializer, ThermohygrometerDataSerializer,
    LatestCCCLGeneratorDataSerializer, CCCLGeneratorSerializer, CCCLEnvironmentSerializer, LatestCCCLEnvironmentDataSerializer)
from pop.models import POP, POPDevice, POPDeviceState

from pop.ups_model import UpsModel
from pop.serializers import UpsModelSerializer 
from pop.solar_model import SolarReading
from pop.serializers import SolarReadingSerializer
from django.utils import timezone
from datetime import timedelta, datetime


class POPViewOnly(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = POPSerializer
    # queryset = POP.objects.filter(is_active=True)
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'network_status', 'user__id']
    search_fields = ['code', 'name']
    http_method_names = ['get', 'head']

    # dynamically set queryset
    def get_queryset(self):
        return self.request.user.user_pops.filter(is_active=True)

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    # dynamically set queryset
    # def get_queryset(self):
    #     return self.request.user.user_pops.filter(is_active=True)

    # def list(self, request):
    #     queryset = self.filter_queryset(self.get_queryset())
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance).data
    #     pops = PopDevice.objects.filter(pop__id=instance.id)
    #     serializer_pop_devices = PopDeviceSerializer(pops, many=True).data
    #     serializer['pops'] = serializer_pop_devices
    #     return Response(serializer)


class POPDeviceViewOnly(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = POPDeviceSerializer
    queryset = POPDevice.objects.filter(is_active=True)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'pop_name']
    search_fields = ['code', 'name']
    http_method_names = ['get', 'head']

    def get_queryset(self):
        pop_ids = [str(pop.id) for pop in self.request.user.user_pops.filter(is_active=True)]
        pops = POPDevice.objects.filter(pop_name__id__in=pop_ids)  # Here, pop_name is attributeName
        return pops


    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    


class POPDeviceStatesViewSet(viewsets.ModelViewSet): 
    queryset = POPDeviceState.objects.filter(is_active=True)
    serializer_class = POPDeviceStatesSerializer
    permission_classes = (IsAuthenticated, )
    http_method_names = ['get', 'head']

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)



class LatestRTDataViewSet(viewsets.ModelViewSet): 
    
    permission_classes = (IsAuthenticated, )
    serializer_class = LatestRTDataSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['topic', 'device_code__code', 'time_range']
    http_method_names = ['get', 'head']

    def get_queryset(self):
        queryset = POPDeviceState.objects.filter(is_active=True)

        # Extract filter parameters from URL
        device_code =  self.request.query_params.get('device_code', '3071523B00003')
        topic =  self.request.query_params.get('topic', 'MQTT_RT_DATA')
        time_range = 'TODAY'
        
        queryset = queryset.filter(device_code__code=device_code, topic=topic, time_range=time_range)

        return queryset


    def list(self, request):
        filtered_queryset = self.filter_queryset(self.get_queryset())
        if filtered_queryset.exists():
            serializer = self.get_serializer(filtered_queryset, many=True).data

        return Response(serializer)
    

class LatestCCCLGeneratorDataViewSet(viewsets.ModelViewSet): 
    
    permission_classes = (IsAuthenticated, )
    serializer_class = LatestCCCLGeneratorDataSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['topic', 'device_code__code', 'time_range']
    http_method_names = ['get', 'head']

    def get_queryset(self):
        queryset = POPDeviceState.objects.filter(is_active=True)

        # Extract filter parameters from URL
        device_code =  self.request.query_params.get('device_code', '3071523B00003')
        topic =  self.request.query_params.get('topic', 'CCCL/PURBACHAL/ENM_01')
        time_range = 'TODAY'
        
        queryset = queryset.filter(device_code__code=device_code, topic=topic, time_range=time_range)

        return queryset


    def list(self, request):
        filtered_queryset = self.filter_queryset(self.get_queryset())
        if filtered_queryset.exists():
            serializer = self.get_serializer(filtered_queryset, many=True).data

        return Response(serializer)
    

class LatestCCCLGeneratorDataViewSet(viewsets.ModelViewSet): 
    
    permission_classes = (IsAuthenticated, )
    serializer_class = LatestCCCLGeneratorDataSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['topic', 'device_code__code', 'time_range']
    http_method_names = ['get', 'head']

    def get_queryset(self):
        queryset = POPDeviceState.objects.filter(is_active=True)

        # Extract filter parameters from URL
        device_code =  self.request.query_params.get('device_code', 'GREEN_POWER_GENERATOR')
        topic =  self.request.query_params.get('topic', 'CCCL/PURBACHAL/ENM_01')
        time_range = 'TODAY'
        
        queryset = queryset.filter(device_code__code=device_code, topic=topic, time_range=time_range)

        return queryset


    def list(self, request):
        filtered_queryset = self.filter_queryset(self.get_queryset())
        if filtered_queryset.exists():
            serializer = self.get_serializer(filtered_queryset, many=True).data

        return Response(serializer)
    

class LatestCCCLEnvironmentDataViewSet(viewsets.ModelViewSet): 
    
    permission_classes = (IsAuthenticated, )
    serializer_class = LatestCCCLEnvironmentDataSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['topic', 'device_code__code', 'time_range']
    http_method_names = ['get', 'head']

    def get_queryset(self):
        queryset = POPDeviceState.objects.filter(is_active=True)

        # Extract filter parameters from URL
        device_code =  self.request.query_params.get('device_code', 'GREEN_POWER_THERMOHYGROMETER')
        topic =  self.request.query_params.get('topic', 'CCCL/PURBACHAL/ENV_01')
        time_range = 'TODAY'
        
        queryset = queryset.filter(device_code__code=device_code, topic=topic, time_range=time_range)

        return queryset


    def list(self, request):
        filtered_queryset = self.filter_queryset(self.get_queryset())
        if filtered_queryset.exists():
            serializer = self.get_serializer(filtered_queryset, many=True).data

        return Response(serializer)
    


class LatestEnyNowDataViewSet(viewsets.ModelViewSet): 
    
    permission_classes = (IsAuthenticated, )
    serializer_class = LatestEnyNowDataSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['topic', 'device_code__code', 'time_range']
    http_method_names = ['get', 'head']

    def get_queryset(self):
        queryset = POPDeviceState.objects.filter(is_active=True)

        # Extract filter parameters from URL
        device_code =  self.request.query_params.get('device_code', '3071523B00003')
        topic =  self.request.query_params.get('topic', 'MQTT_ENY_NOW')
        time_range = 'TODAY'
        
        queryset = queryset.filter(device_code__code=device_code, topic=topic, time_range=time_range)

        return queryset


    def list(self, request):
        filtered_queryset = self.filter_queryset(self.get_queryset())
        if filtered_queryset.exists():
            serializer = self.get_serializer(filtered_queryset, many=True).data

        return Response(serializer)
    


class LatestThermohygrometerDataViewSet(viewsets.ModelViewSet): 
    
    permission_classes = (IsAuthenticated, )
    serializer_class = LatestThermohygrometerDataSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['topic', 'device_code__code', 'time_range']
    http_method_names = ['get', 'head']

    def get_queryset(self):
        queryset = POPDeviceState.objects.filter(is_active=True)

        # Extract filter parameters from URL
        device_code =  self.request.query_params.get('device_code', 'COLOCITY_THERMOHYGROMETER')
        topic =  self.request.query_params.get('topic', 'DCIM/COLOCITY/ENV_01')
        time_range = 'TODAY'
        
        queryset = queryset.filter(device_code__code=device_code, topic=topic, time_range=time_range)

        return queryset


    def list(self, request):
        filtered_queryset = self.filter_queryset(self.get_queryset())
        if filtered_queryset.exists():
            serializer = self.get_serializer(filtered_queryset, many=True).data

        return Response(serializer)
    

class CCCLGeneratorViewSet(viewsets.ModelViewSet): 
    
    permission_classes = (IsAuthenticated, )
    serializer_class = CCCLGeneratorSerializer 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['topic', 'device_code__code', 'time_range']
    http_method_names = ['get', 'head']

    def get_queryset(self):
        queryset = POPDeviceState.objects.filter(is_active=True)

        # Extract filter parameters from URL
        device_code =  self.request.query_params.get('device_code', None)
        topic =  self.request.query_params.get('topic', None)
        time_range =  self.request.query_params.get('time_range', None)

        if device_code:
            queryset = queryset.filter(device_code__code=device_code)
        elif device_code and topic:
            queryset = queryset.filter(device_code__code=device_code, topic=topic)
        elif device_code and topic and time_range:
            queryset = queryset.filter(device_code__code=device_code, topic=topic, time_range=time_range)

        return queryset
    

class CCCLEnvironmentViewSet(viewsets.ModelViewSet): 
    
    permission_classes = (IsAuthenticated, )
    serializer_class = CCCLEnvironmentSerializer 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['topic', 'device_code__code', 'time_range']
    http_method_names = ['get', 'head']

    def get_queryset(self):
        queryset = POPDeviceState.objects.filter(is_active=True)

        # Extract filter parameters from URL
        device_code =  self.request.query_params.get('device_code', None)
        topic =  self.request.query_params.get('topic', None)
        time_range =  self.request.query_params.get('time_range', None)

        if device_code:
            queryset = queryset.filter(device_code__code=device_code)
        elif device_code and topic:
            queryset = queryset.filter(device_code__code=device_code, topic=topic)
        elif device_code and topic and time_range:
            queryset = queryset.filter(device_code__code=device_code, topic=topic, time_range=time_range)

        return queryset
    

class CPMDataViewSet(viewsets.ModelViewSet): 
    
    permission_classes = (IsAuthenticated, )
    serializer_class = CPMDataSerializer 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['topic', 'device_code__code', 'time_range']
    http_method_names = ['get', 'head']

    def get_queryset(self):
        queryset = POPDeviceState.objects.filter(is_active=True)

        # Extract filter parameters from URL
        device_code =  self.request.query_params.get('device_code', None)
        topic =  self.request.query_params.get('topic', None)
        time_range =  self.request.query_params.get('time_range', None)

        if device_code:
            queryset = queryset.filter(device_code__code=device_code)
        elif device_code and topic:
            queryset = queryset.filter(device_code__code=device_code, topic=topic)
        elif device_code and topic and time_range:
            queryset = queryset.filter(device_code__code=device_code, topic=topic, time_range=time_range)

        return queryset


class ThermohygrometerDataViewSet(viewsets.ModelViewSet): 
    
    permission_classes = (IsAuthenticated, )
    serializer_class = ThermohygrometerDataSerializer 
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['topic', 'device_code__code', 'time_range']
    http_method_names = ['get', 'head']

    def get_queryset(self):
        queryset = POPDeviceState.objects.filter(is_active=True)

        # Extract filter parameters from URL
        device_code =  self.request.query_params.get('device_code', None)
        topic =  self.request.query_params.get('topic', None)
        time_range =  self.request.query_params.get('time_range', None)

        if device_code:
            queryset = queryset.filter(device_code__code=device_code)
        elif device_code and topic:
            queryset = queryset.filter(device_code__code=device_code, topic=topic)
        elif device_code and topic and time_range:
            queryset = queryset.filter(device_code__code=device_code, topic=topic, time_range=time_range)

        return queryset
    

class MinuteLevelDataView(viewsets.ModelViewSet):
    serializer_class = MinuteLevelDataSerializer
    permission_classes = (IsAuthenticated, )
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['topic', 'device_code__code', 'time_range']
    http_method_names = ['get', 'head']

    def get_queryset(self):
        queryset = POPDeviceState.objects.filter(is_active=True)

        # Extract filter parameters from URL
        device_code =  self.request.query_params.get('device_code', None)
        topic =  self.request.query_params.get('topic', None)
        time_range =  self.request.query_params.get('time_range', None)

        if device_code:
            queryset = queryset.filter(device_code__code=device_code)
        elif device_code and topic:
            queryset = queryset.filter(device_code__code=device_code, topic=topic)
        elif device_code and topic and time_range:
            queryset = queryset.filter(device_code__code=device_code, topic=topic, time_range=time_range)

        return queryset
    
    

class UpsDataViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UpsModelSerializer


    def get_queryset(self):
        queryset = UpsModel.objects.using("nonrel").all()
        print("Count from Django ORM (before filtering):", queryset.count())

        time_range = self.request.query_params.get('time_range', None)
        print("Time range:", time_range)

        if time_range:
            now = timezone.now()

            if time_range == 'TODAY':
                start_time = timezone.datetime(now.year, now.month, now.day, 0, 0, 0, tzinfo=timezone.utc)
            elif time_range == "LAST_7_DAYS":
                start_time = now - timedelta(days=7)
            elif time_range == "LAST_30_DAYS":
                start_time = now - timedelta(days=30)
            elif time_range == "THIS_YEAR":
                start_time = timezone.datetime(now.year, 1, 1, tzinfo=timezone.utc)
            else:
                return queryset

            # Convert start_time to ISO 8601 format without timezone (to match MongoDB format)
            start_time_iso = start_time.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3]  # Remove timezone and trim microseconds
            print("Start time (ISO format without timezone):", start_time_iso)

            # Debug: Print the first few timestamps from MongoDB
            print("First few timestamps from MongoDB:", queryset[:5].values_list('timestamp', flat=True))

            # Filter queryset where timestamp is greater than or equal to start_time_iso
            queryset = queryset.filter(timestamp__gte=start_time_iso)

        print("Count from Django ORM (after filtering):", queryset.count())
        return queryset


    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
    


import pytz

class SolarReadingsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = SolarReadingSerializer

    def get_queryset(self):
        queryset = SolarReading.objects.using("nonrel").all()
        print("Count from Django ORM (before filtering):", queryset.count())

        time_range = self.request.query_params.get('time_range', None)
        print("Time range:", time_range)

        if time_range:
            now = timezone.now()  # Use timezone-aware `now`

            # Set timezone to Asia/Dhaka (UTC+6)
            dhaka_tz = pytz.timezone('Asia/Dhaka')

            if time_range == 'TODAY':
                start_time = timezone.datetime(now.year, now.month, now.day, 0, 0, 0, tzinfo=dhaka_tz)
            elif time_range == "LAST_7_DAYS":
                start_time = now - timedelta(days=7)
            elif time_range == "LAST_30_DAYS":
                start_time = now - timedelta(days=30)
            elif time_range == "THIS_YEAR":
                start_time = timezone.datetime(now.year, 1, 1, tzinfo=dhaka_tz)
            else:
                return queryset

            # Ensure `start_time` is timezone-aware (Asia/Dhaka)
            if timezone.is_naive(start_time):
                start_time = timezone.make_aware(start_time, timezone=dhaka_tz)

            # Convert start_time to ISO 8601 format with timezone
            start_time_iso = start_time.isoformat()  # Django timezone-aware datetime
            print("Start time (ISO format with timezone):", start_time_iso)

            # Debug: Print the first few timestamps from MongoDB
            print("First few timestamps from MongoDB:", queryset[:5].values_list('timestamp', flat=True))

            # Filter queryset where timestamp is greater than or equal to start_time
            queryset = queryset.filter(timestamp__gte=start_time)

        print("Count from Django ORM (after filtering):", queryset.count())
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
