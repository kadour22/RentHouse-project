from rest_framework import serializers
from .models import (
    Tenant , Department , House , HouseImage , Rent
)

class TenantSerializer(serializers.ModelSerializer) :
    class Meta :
        model  = Tenant
        fields = [
            'username'    ,      
            'email',         
            'phone_number',     
            'is_staff',          
            'age'    ,         
            'identity_card_num' ,
            'is_active'  ,       
            'sec_field'   ,      
            'created_at'    ,    
            'updated_at'       
        ]
class DepartmentSerializer(serializers.ModelSerializer) :
    class meta :
        model = Department
        fields = [
            "name",
            "location",
        ]

class HouseSerializer(serializers.ModelSerializer) :
    class Meta :
        model = House
        fields = [
            "description" , 
            "type" ,
            "price_per_month" ,
            "available" , 
            "department"
        ]

class RentSerializer(serializers.ModelSerializer) :
    class Meta :
        model  = Rent
        fields = [
            "house" , 
            "tenant",
        ]
