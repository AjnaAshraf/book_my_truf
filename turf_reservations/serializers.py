from rest_framework import serializers

class BookingsSerializers(serializers.Serializer):

    team = serializers.CharField()

    phone_number = serializers.CharField()

    turf = serializers.CharField()

    date = serializers.DateField()

    email = serializers.EmailField()

    match_time = serializers.TimeField(read_only = True)

    match_duration = serializers.DurationField(read_only = True)

    created_at = serializers.DateTimeField(read_only = True)