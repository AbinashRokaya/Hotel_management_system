from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import HotelSerializer
from .models import Hotel
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class Hotel_Views(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        hotel_list = Hotel.objects.all()
        serializer = HotelSerializer(hotel_list,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = HotelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)
        
class Hotel_Details(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,pk):
        try:
            hotel=Hotel.objects.get(id=pk)
        except Hotel.DoesNotExist:
            return Response({'error':'Not Found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = HotelSerializer(hotel)
        return Response(serializer.data)
    
    def put(self,request,pk):
        hotel = Hotel.objects.get(id=pk)
        serializer = HotelSerializer(hotel,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,pk):
        hotel = Hotel.objects.get(id=pk)
        hotel.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

