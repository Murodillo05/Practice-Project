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
