from django.urls import path
from . import views

urlpatterns=[
    path('guest_views/',views.Guest_Views.as_view(),name='guest_view'),
    path('guest_views/<int:pk>/',views.Guest_Details.as_view()),
    path('guest_views/<int:pk>/reservation',views.GuestReservation_views.as_view())

]