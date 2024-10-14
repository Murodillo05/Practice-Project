from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('Discounts/', DiscountsCreate.as_view(), name="discounts-"),
    path("Discount/", GetDiscount.as_view(),name="discounts"),
    path('about/', AboutView.as_view(), name='about-view'),
    path('services/', ServiceView.as_view(), name='service-view'),
    path('programinfo/', ProgramInfoView.as_view(), name='program-info'),
    path('programinfo2/', ProgramInfoCreateView.as_view(), name='program-info-create'),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)