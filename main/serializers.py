from .models import *
from rest_framework import serializers
class DiscountsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Discounts
        fields = 'all'

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        models = About
        fields = '_all__'



class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'