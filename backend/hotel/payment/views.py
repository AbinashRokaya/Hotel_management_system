from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import PaymentSerializer
from reservation.serializer import ReservationSerializer
from .models import Payment
from reservation.models import Reservation
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
class Payment_Views(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request):
        payment_list = Payment.objects.all()
        serializer = PaymentSerializer(payment_list,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)
        
class Payment_Details(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,pk):
        try:
            payment=Payment.objects.get(id=pk)
        except Payment.DoesNotExist:
            return Response({'error':'Not Found'},status=status.HTTP_404_NOT_FOUND)
        
        serializer = PaymentSerializer(payment)
        return Response(serializer.data)
    
    def put(self,request,pk):
        payment = Payment.objects.get(id=pk)
        serializer = PaymentSerializer(payment,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        

    def delete(self,request,pk):
        payment = Payment.objects.get(id=pk)
        payment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PaymentReservation_views(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self,request,pk):
        try:
            reservation = Reservation.objects.get(id=pk)
        except Reservation.DoesNotExist:
             return Response({'error':'Not Found'},status=status.HTTP_404_NOT_FOUND)
        
        reservation = reservation.reservation_id.all()
        serializer= PaymentSerializer(reservation,many=True)
        return Response(serializer.data)
