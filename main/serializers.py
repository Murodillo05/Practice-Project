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

# class AboutSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = About
#         fields = '_   _all__'

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About  # This should be your model name
        fields = '__all__'  # Or specify the fields you want to include

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'
        

class DiscountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discounts
        fields = '__all__' # You can specify fields explicitly if needed