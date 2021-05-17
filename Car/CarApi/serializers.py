from rest_framework import serializers
from .models import Company,Car,Feature,Specification
from django.contrib.auth.models import User

class CompanySerializer(serializers.ModelSerializer):    
    carCount = serializers.SerializerMethodField()
    class Meta:
        model = Company 
        fields = ('id','name','established','carCount')
   
    def get_carCount(self,obj):
        id = obj.id
        cars = Car.objects.filter(company_id=id)   
        return cars.count()
        


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields =  ('__all__')
       


class CarSerializer(serializers.ModelSerializer):
    car_spec =  serializers.SerializerMethodField('get_car_spec')
    class Meta:
        model = Car
        fields = ('id','name','features','company','published_by','car_spec')  

    def get_car_spec(self,obj):
        id = obj.id
        return Specification.objects.filter(car=id).values()

  
class CarReadSerializer(serializers.ModelSerializer):
    car_spec =  serializers.SerializerMethodField('get_car_spec')
    features = serializers.StringRelatedField(many=True)
    published_by = serializers.StringRelatedField()
    company = serializers.StringRelatedField()
    class Meta:
        model = Car
        fields = ('id','name','features','company','published_by','car_spec')  
        depth = 1

    def get_car_spec(self,obj):
        id = obj.id
        return Specification.objects.filter(car=id).values()
        
    def get_published_by(self,obj):
        print('obj__',obj)
        return obj.user.username
        

class SpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = ('__all__')

