from django.urls import path
from . import views

urlpatterns = [
    path('Discounts/', views.discounts),
    path('about/', views.about_view),
    path('service/', views.service_view),
    path('programinfo/', views.programinfo, name='program_info'),
    path('program/', views.program, name='program'),
    path('questions/', views.questions, name='questions'),
    path('testimonal/', views.testimonal, name='testimonal'),
    path('apartments/', views.apartments, name='apartments'),
    path('apartments_info/', views.apartmentsinfo, name='apartments_info')
]