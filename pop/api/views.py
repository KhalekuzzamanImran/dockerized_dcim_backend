from rest_framework import viewsets, filters, status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics

from django_filters.rest_framework import DjangoFilterBackend

from pop.api.serializers import (
    POPSerializer, POPDeviceSerializer, POPDeviceStatesSerializer,
    LatestRTDataSerializer, LatestEnyNowDataSerializer, LatestThermohygrometerDataSerializer,
    CPMDataSerializer, MinuteLevelDataSerializer, ThermohygrometerDataSerializer)
from pop.models import POP, POPDevice, POPDeviceState



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
        device_code =  self.request.query_params.get('device_code', 'ModhumatiBank-ENV_01')
        topic =  self.request.query_params.get('topic', 'DCIM/ModhumatiBank/ENV_01')
        time_range = 'TODAY'
        
        queryset = queryset.filter(device_code__code=device_code, topic=topic, time_range=time_range)

        return queryset


    def list(self, request):
        filtered_queryset = self.filter_queryset(self.get_queryset())
        if filtered_queryset.exists():
            serializer = self.get_serializer(filtered_queryset, many=True).data

        return Response(serializer)
    

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