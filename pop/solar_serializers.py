from rest_framework import serializers

class SolarReadingSerializer(serializers.Serializer):
    _id = serializers.CharField()
    current = serializers.ListField(child=serializers.FloatField(), required=False)
    power = serializers.ListField(child=serializers.FloatField(), required=False)
    energy_consumption = serializers.ListField(child=serializers.IntegerField(), required=False)  # Add the energy_consumption field
    timestamp = serializers.CharField(required=False)  # Add the timestamp field
