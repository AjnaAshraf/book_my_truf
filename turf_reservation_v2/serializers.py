from rest_framework import serializers
from turf_reservation_v2.models import Booking
from django.contrib.auth.models import User
from datetime import datetime,timedelta

class BookingSerializer(serializers.ModelSerializer):

    turf = serializers.StringRelatedField()

    class Meta:

        model = Booking

        fields ="__all__"

        read_only_fields = ["id","end_time"]

    def validate(self, validated_data):

        date = validated_data.get("date")

        if date < datetime.today().date():

            raise serializers.ValidationError(
                "Invalid booking date. Please enter a valid future date."
            )

        match_duration = validated_data.get("match_duration")

        if match_duration<timedelta(hours=1):

                raise serializers.ValidationError("........The minimum match duration must be 1 hour........")

        return validated_data

class SignupSerilaizer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ["username","email","password"]




            
