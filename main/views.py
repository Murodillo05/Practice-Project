from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . models import  About, Service
from .serializers import AboutSerializer, ServiceSerializer



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