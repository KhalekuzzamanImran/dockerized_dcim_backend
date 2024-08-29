from pop.api.views import (
    POPViewOnly, POPDeviceViewOnly, POPDeviceStatesViewSet,
    LatestRTDataViewSet, LatestEnyNowDataViewSet, LatestThermohygrometerDataViewSet,
    CPMDataViewSet, MinuteLevelDataView,ThermohygrometerDataViewSet )
from django.urls import path, include

from rest_framework import routers

app_name = 'pops'

router = routers.DefaultRouter()
router.register(r'pops', POPViewOnly, 'get_pops')
router.register(r'pop-devices', POPDeviceViewOnly, 'get_pop_devices')
router.register(r'pop-device-states', POPDeviceStatesViewSet, 'get_device_states')
router.register(r'cpm-latest-rt-data', LatestRTDataViewSet, 'get_latest_rt_data')
router.register(r'cpm-data', CPMDataViewSet, 'get_device_state_history')
router.register(r'cpm-latest-enynow-data', LatestEnyNowDataViewSet, 'get_enynow_latest_data')
router.register(r'cpm-enynow-data', MinuteLevelDataView, 'get_enynow_history_data')
router.register(r'thermohygrometer-latest-data', LatestThermohygrometerDataViewSet, 'get_thermohygrometer_latest_data')
router.register(r'thermohygrometer-data', ThermohygrometerDataViewSet, 'get_thermohygrometer_data')

urlpatterns = [
    path('', include(router.urls)),
]
