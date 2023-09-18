from rest_framework import serializers
from .models import TV, simCard
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User 

class TVSerializer(serializers.ModelSerializer):
    class Meta:
        model=TV
        fields=('name', 'SN', 'user')

    def create(self, validated_data):
        validated_data['user']=get_object_or_404(User, username=self.context['request'].user)
        return super(TVSerializer, self).create(validated_data)

class simCardSerializer(serializers.ModelSerializer):
    class Meta:
        model=simCard
        fields=('comName', 'number', 'user')

    def create(self, validated_data):
        validated_data['user']=get_object_or_404(User, username=self.context['request'].user)
        return super(simCardSerializer, self).create(validated_data)