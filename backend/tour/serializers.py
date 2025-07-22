from rest_framework import serializers
from .models import Destination

class DestinationSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)

    class Meta:
        model = Destination
        fields = '__all__'

