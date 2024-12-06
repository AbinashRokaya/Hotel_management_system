from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import RoomSerializer
from reservation.serializer import ReservationSerializer
from hot.serializer import HotelSerializer
from hot.models import Hotel
from .models import Room
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


# Create your views here.
class Room_Views(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        room_list = Room.objects.all()
        serializer = RoomSerializer(room_list,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class Room_Details(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,pk):
        try:
            room=Room.objects.get(id=pk)
        except Room.DoesNotExist:
            return Response({'error':'Not Found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = RoomSerializer(room)
        return Response(serializer.data)
    
    def put(self,request,pk):
        room = Room.objects.get(id=pk)
        serializer = RoomSerializer(room,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,pk):
        room = Room.objects.get(id=pk)
        room.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class HotelRoom_views(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,pk):
        try:
            hotels = Hotel.objects.get(id=pk)
        except Room.DoesNotExist:
             return Response({'error':'Not Found'},status=status.HTTP_404_NOT_FOUND)
        
        rooms = hotels.rooms.all()
        serializer= RoomSerializer(rooms,many=True)
        return Response(serializer.data)

