from pop.api.views import (
    POPViewOnly, POPDeviceViewOnly, POPDeviceStatesViewSet,
    LatestRTDataViewSet, LatestEnyNowDataViewSet, LatestThermohygrometerDataViewSet,
    CPMDataViewSet, MinuteLevelDataView,ThermohygrometerDataViewSet, LatestCCCLGeneratorDataViewSet, CCCLGeneratorViewSet, CCCLEnvironmentViewSet, LatestCCCLEnvironmentDataViewSet,
    UpsDataViewSet)
from pop.solar_views import SolarReadingViewSet, SolarEnergyConsumptionViewSet
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

router.register(r'cccl-generator-latest-data', LatestCCCLGeneratorDataViewSet, 'get_cccl_generator_latest_data')
router.register(r'cccl-generator-data', CCCLGeneratorViewSet, 'get_cccl_generator_history_data')

router.register(r'cccl-environment-latest-data', LatestCCCLEnvironmentDataViewSet, 'get_cccl_environment_latest_data')
router.register(r'cccl-environment-data', CCCLEnvironmentViewSet, 'get_cccl_environment_history_data')

router.register(r'ups-data', UpsDataViewSet, 'get_ups_data')
# router.register(r'solar-readings', SolarReadingsViewSet, 'get_solar_data')
router.register(r'solar-readings', SolarReadingViewSet, 'solar-readings')
router.register(r'solar-energy-consumption', SolarEnergyConsumptionViewSet, 'solar-readings')

urlpatterns = [
    path('', include(router.urls)),
]
