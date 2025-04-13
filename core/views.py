from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status , permissions

from .models import Tenant  , House , Department
from .serializers import TenantSerializer , RentSerializer , HouseSerializer , DepartmentSerializer

# Tenant Logic

class CreatetenantView(APIView) :
    permission_classes = [permissions.AllowAny]
    # throttle_classes = []
    def post(self , request , *args , **kwargs) :
        serializer = TenantSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

class ListTenantView(APIView) :
    permission_classes = [permissions.IsAdminUser]
    # throttle_classes = []
    def get(self , request , *args , **kwargs) :
        tenants = Tenant.objects.all()
        serializer = TenantSerializer(tenants , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)

class RetrieveTenantView(APIView) :
    permission_classes = [permissions.IsAdminUser]
    # throttle_classes = []
    def get(self , request , tenant_id , *args , **kwargs) :
        try :
            tenant = Tenant.objects.get(id=tenant_id)
        except Tenant.DoesNotExist :
            return Response({"detail" : "Tenant not found"} , status=status.HTTP_404_NOT_FOUND)
        serializer = TenantSerializer(tenant)
        return Response(serializer.data , status=status.HTTP_200_OK)

# Rent Logic

class RentHouseView(APIView) :
    
    # permission_classes = [permissions.IsAuthenticated]
    def post(self , request , *args , **kwargs) :
        serializer = RentSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

class AddDepartmentView(APIView) :
    
    def post(self , request , *args , **kwargs) :
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

class AddHouseView(APIView) :
    def post(self , request , *args , **kwargs) :
        serializer = HouseSerializer(data=request.data) 
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else :
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class ListHouseView(APIView) :
    permission_classes = [permissions.IsAdminUser]
    def get(self , request , *args , **kwargs) :
        houses = House.objects.all()
        serializer = HouseSerializer(houses , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)

class RetrieveHouseView(APIView) :
    permission_classes = [permissions.IsAdminUser]
    def get(self , request , house_id , *args , **kwargs) :
        try :
            house = House.objects.get(id=house_id)
        except House.DoesNotExist :
            return Response({"detail" : "House not found"} , status=status.HTTP_404_NOT_FOUND)
        serializer = HouseSerializer(house)
        return Response(serializer.data , status=status.HTTP_200_OK)