from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Company,Feature,Car,Specification
from .serializers import CompanySerializer,FeatureSerializer,CarSerializer,SpecificationSerializer,CarReadSerializer
from rest_framework import status
from django.contrib.auth.models import User
# Create your views here.

class CompanyView(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

class FeatureView(viewsets.ModelViewSet):
    serializer_class = FeatureSerializer  
    queryset = Feature.objects.all()
   

class CarView(viewsets.ModelViewSet):
    # serializer_class = CarSerializer
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CarReadSerializer
        return CarSerializer        
    queryset = Car.objects.all()
        

class SpecificationView(viewsets.ModelViewSet):
    serializer_class = SpecificationSerializer
    queryset = Specification.objects.all()
  


