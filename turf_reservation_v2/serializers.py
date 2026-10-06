from rest_framework import serializers
from turf_reservation_v2.models import Booking
from django.contrib.auth.models import User

class BookingSerializer(serializers.ModelSerializer):

    class Meta:

        model = Booking

        fields ="__all__"

class SignupSerilaizer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["username","email","password"]