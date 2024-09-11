from rest_framework import serializers
from .models import *

class Program_infoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program_info
        fields = '__all__'


class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = '__all__'



class TestimonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonal
        fields = '__all__'

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

