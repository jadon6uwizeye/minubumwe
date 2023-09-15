from rest_framework import serializers
from .models import Request, Sector

class RequestSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Request
        fields = '__all__'
        # hide approved
        extra_kwargs = {'approved': {'read_only': True}}

class SectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sector
        fields = '__all__'