from rest_framework import serializers
from .ups_model import UpsModel, DataItem

class DataItemSerializer(serializers.Serializer):
    oid = serializers.CharField()
    name = serializers.CharField()
    value = serializers.CharField()

class UpsModelSerializer(serializers.ModelSerializer):
    data = serializers.ListField(child=DataItemSerializer())

    class Meta:
        model = UpsModel
        fields = ['_id', 'timestamp', 'data']
