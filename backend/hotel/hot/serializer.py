from rest_framework import serializers
from hot.models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hotel
        fields = "__all__"

        