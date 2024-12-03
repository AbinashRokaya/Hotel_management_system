from django.urls import path
from . import views

urlpatterns=[
    path('payment_view/',views.Payment_Views.as_view()),
    path('payment_view/<int:pk>/',views.Payment_Details.as_view()),
    path('payment_view/<int:pk>/reservations/',views.PaymentReservation_views.as_view()),
    

]