from rest_framework import serializers
from .models import TV, simCard

class TVSerializer(serializers.ModelSerializer):
    class Meta:
        model=TV
        fields=('name', 'SN')

class simCardSerializer(serializers.ModelSerializer):
    class Meta:
        model=simCard
        fields=('comName', 'number')