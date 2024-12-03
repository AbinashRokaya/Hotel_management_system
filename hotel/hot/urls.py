from django.urls import path
from . import views

urlpatterns=[
    path('hotel_views/',views.Hotel_Views.as_view(),name='hotelViews'),
    path('hotel_views/<int:pk>/',views.Hotel_Details.as_view(),name='hotelViews')
]
