from django.urls import path
from . import views

urlpatterns=[
    path('room_views/',views.Room_Views.as_view(),name='room_views'),
    path('room_views/<int:pk>/',views.Room_Details.as_view(),name='room_details'),
    path('room_views/<int:pk>/hotel/',views.HotelRoom_views.as_view(),name='roomreservation')
]