from django.urls import path
from . import views

urlpatterns = [
    path('discounts/', views.Discounts_get),
    path('about/', views.about_view),
    path('service/', views.service_view),
]