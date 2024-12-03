from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import ReservationSerializer
from room.serializer import RoomSerializer
from .models import Reservation
from room.models import Room
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class Reservation_Views(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        reservation_list = Reservation.objects.all()
        serializer = ReservationSerializer(reservation_list,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)
        
class Reservation_Details(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,pk):
        try:
            guest=Reservation.objects.get(id=pk)
        except Reservation.DoesNotExist:
            return Response({'error':'Not Found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = ReservationSerializer(guest)
        return Response(serializer.data)
    
    def put(self,request,pk):
        reservation = Reservation.objects.get(id=pk)
        serializer = ReservationSerializer(reservation,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,pk):
        guest = Reservation.objects.get(id=pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReservationRoom_views(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,pk):
        try:
            rooms = Room.objects.get(id=pk)
        except Room.DoesNotExist:
             return Response({'error':'Not Found'},status=status.HTTP_404_NOT_FOUND)
        
        reservation = rooms.room_id.all()
        serializer= ReservationSerializer(reservation,many=True)
        return Response(serializer.data)
