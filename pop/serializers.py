from rest_framework import serializers
from .ups_model import UpsModel, DataItem
from .solar_model import SolarReading, CurrentData, PowerData, EnergyConsumption

class DataItemSerializer(serializers.Serializer):
    oid = serializers.CharField()
    name = serializers.CharField()
    value = serializers.CharField()

class UpsModelSerializer(serializers.ModelSerializer):
    data = serializers.ListField(child=DataItemSerializer())

    class Meta:
        model = UpsModel
        fields = ['_id', 'timestamp', 'data']



class CurrentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentData
        fields = ['values']

class PowerDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerData
        fields = ['values']

class EnergyConsumptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnergyConsumption
        fields = ['values']

class SolarReadingSerializer(serializers.ModelSerializer):
    current = CurrentDataSerializer()
    power = PowerDataSerializer()
    energy_consumption = EnergyConsumptionSerializer()

    class Meta:
        model = SolarReading
        fields = ['_id', 'timestamp', 'current', 'power', 'energy_consumption']

