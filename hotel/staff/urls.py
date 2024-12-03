from django.urls import path
from . import views

urlpatterns=[
    path('staff_view/',views.Staff_Views.as_view()),
    path('staff_view/<int:pk>/',views.Staff_Details.as_view()),

]