from django.urls import path
from . import views

urlpatterns=[
    path('reservation_views/',views.Reservation_Views.as_view()),
    path('reservation_views/<int:pk>/',views.Reservation_Details.as_view()),
    path('reservation_views/<int:pk>/room/',views.ReservationRoom_views.as_view()),
]