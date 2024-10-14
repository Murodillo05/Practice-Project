from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated


from rest_framework.views import APIView

from .models import *
from drf_yasg.utils import swagger_auto_schema

class ProgramInfoView(APIView):

    @swagger_auto_schema(
        responses={200: Program_infoSerializer(many=True)}
    )
    def get(self, request):
        program_info = Program_info.objects.filter(is_active=True)
        program_info_ser = Program_infoSerializer(program_info, many=True)
        return Response(program_info_ser.data)


class ProgramInfoCreateView(generics.CreateAPIView):
    queryset = Program_info.objects.all()
    serializer_class = Program_infoSerializer

    @swagger_auto_schema(
        request_body=Program_infoSerializer,
        responses={201: Program_infoSerializer, 400: 'Bad Request'}
    )
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def program(request):
    if request.method == "GET":
        program = Program.objects.filter(is_active=True)
        program_ser = ProgramSerializer(program, many=True)
        return Response(program_ser.data)

    elif request.method == "POST":
        serializer = ProgramSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def questions(request):
    if request.method == "GET":
        questions = Questions.objects.filter(is_active=True)
        questions_ser = QuestionSerializer(questions, many=True)
        return Response(questions_ser.data)

    elif request.method == "POST":
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def testimonal(request):
    if request.method == "GET":
        testimonal = Testimonal.objects.filter(is_active=True)
        testimonal_ser = TestimonalSerializer(testimonal, many=True)
        return Response(testimonal_ser.data)

    elif request.method == "POST":
        serializer = TestimonalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DiscountsCreate(generics.CreateAPIView):
    queryset = Discounts.objects.all()
    serializer_class = DiscountsSerializer

    @swagger_auto_schema(
        request_body=DiscountsSerializer,
        responses={201: DiscountsSerializer}
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class GetDiscount(APIView):
    @swagger_auto_schema(
        responses={201: DiscountsSerializer(many=True)}
    )
    def get(self, request):
        discounts = Discounts.objects.all() 
        serializer =  DiscountsSerializer(discounts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# @api_view(['GET', 'POST'])
# def discounts(request):
#     if request.method == 'GET':  
#         discounts = Discounts.objects.filter(is_active=True)
#         discounts_serializer = DiscountsSerializers(discounts, many=True)
#         return Response(discounts_serializer.data, status=status.HTTP_200_OK)

#     elif request.method == 'POST':
#         serializer = DiscountsSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AboutView(APIView):

    @swagger_auto_schema(
        responses={200: AboutSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        # Retrieve all active About objects
        banners = About.objects.filter(is_active=True)
        serializer = AboutSerializer(banners, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=AboutSerializer,
        responses={201: AboutSerializer, 400: 'Bad Request'}
    )
    def post(self, request, *args, **kwargs):
        # Create a new About object
        serializer = AboutSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ServiceView(APIView):

    @swagger_auto_schema(
        responses={200: ServiceSerializer(many=True)}
    )
    def get(self, request, *args, **kwargs):
        # Retrieve all active Service objects
        services = Service.objects.filter(is_active=True)
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=ServiceSerializer,
        responses={201: ServiceSerializer, 400: 'Bad Request'}
    )
    def post(self, request, *args, **kwargs):
        # Create a new Service object
        serializer = ServiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
