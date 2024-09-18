<<<<<<< HEAD
from django.shortcuts import render

=======
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *



@api_view(['GET, POST'])
def programinfo(request):
    if request.method == "GET":
        program_info = Program_info.objects.last()
        program_info_ser = Program_infoSerializer(program_info)
        return Response(program_info_ser.data)
    

    elif request.method == "POST":
        serializer = Program_infoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET, POST'])
def program(request):
    if request.method == "GET":
        program = Program.objects.last()
        program_ser = ProgramSerializer(program)
        return Response(program_ser.data)

    elif request.method == "POST":
        serializer = ProgramSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET, POST'])
def questions(request):
    if request.method == "GET":
        questions = Questions.objects.last()
        questions_ser = QuestionSerializer(questions)
        return Response(questions_ser.data)

    elif request.method == "POST":
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def testimonal(request):
    if request.method == "GET":
        testimonal = Testimonal.objects.last()
        testimonal_ser = TestimonalSerializer(testimonal)
        return Response(testimonal_ser.data)

    elif request.method == "POST":
        serializer = TestimonalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 
@api_view(['GET', 'POST'])
def discounts(request):
    if request.method == 'GET':
        discounts = Discounts.objects.all()
        discounts_serializer = DiscountsSerializers(discounts, many=True)
        return Response(discounts_serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = DiscountsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def about_view(request):
    if request.method == 'GET':
        banners = About.objects.get()
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
>>>>>>> c27db3c18948829ec8e5235ab213c708d22e6e4c
