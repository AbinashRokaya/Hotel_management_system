from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import GuestSerializer
from reservation.serializer import ReservationSerializer
from .models import Guest
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class Guest_Views(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        guest_list = Guest.objects.all()
        serializer = GuestSerializer(guest_list,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)
        
class Guest_Details(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,pk):
        try:
            guest=Guest.objects.get(id=pk)
        except Guest.DoesNotExist:
            return Response({'error':'Not Found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = GuestSerializer(guest)
        return Response(serializer.data)
    
    def put(self,request,pk):
        guest = Guest.objects.get(id=pk)
        serializer = GuestSerializer(guest,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,pk):
        guest = Guest.objects.get(id=pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class GuestReservation_views(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,pk):
        try:
            guest = Guest.objects.get(id=pk)
        except Guest.DoesNotExist:
             return Response({'error':'Not Found'},status=status.HTTP_404_NOT_FOUND)
        
        reservation = guest.guest_id.all()
        serializer= ReservationSerializer(reservation,many=True)
        return Response(serializer.data)
