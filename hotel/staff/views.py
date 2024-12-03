from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import StaffSerializer
from .models import Staff
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class Staff_Views(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        staff_list = Staff.objects.all()
        serializer = StaffSerializer(staff_list,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)
        
class Staff_Details(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,pk):
        try:
            guest=Staff.objects.get(id=pk)
        except Staff.DoesNotExist:
            return Response({'error':'Not Found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = StaffSerializer(guest)
        return Response(serializer.data)
    
    def put(self,request,pk):
        staff = Staff.objects.get(id=pk)
        serializer = StaffSerializer(staff,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,pk):
        staff = Staff.objects.get(id=pk)
        staff.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)