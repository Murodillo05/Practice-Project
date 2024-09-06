from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . models import  About, Service, Discounts
from .serializers import AboutSerializer, ServiceSerializer,DiscountsSerializers
from . import serializers
from django.shortcuts import render

@api_view(['GET', 'POST'])
def Discounts_get(request):
    if request.method == 'GET':
     discounts = Discounts.objects.all()
     Discounts_ser = DiscountsSerializers(discounts, many = True)
     return Response(Discounts_ser.data, status=status.HTTP_200_OK)


def Discounts_post(self, request):
    if request.method == 'POST':
       discounts = Discounts_post.all()
       Discounts_ser = DiscountsSerializers(discounts, many = True)
       return Response(Discounts_ser.data , status=status.HTTP_201_CREATED)
    return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def about_view(request):
    if request.method == 'GET':
        banners = About.objects.all()
        serializer = AboutSerializer(banners, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = AboutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'POST'])
def service_view(request):
    if request.method == 'GET':
        banners = Service.objects.all()
        serializer = ServiceSerializer(banners, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)