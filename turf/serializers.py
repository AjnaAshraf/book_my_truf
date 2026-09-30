from rest_framework import serializers


class TurfSerializers(serializers.Serializer):

    id = serializers.CharField(read_only = True)

    name = serializers.CharField()

    location = serializers.CharField()

    phone = serializers.CharField()

    fee = serializers.IntegerField()



    def validate(self,validated_data):

        fee = validated_data.get("fee")

        if fee< 500:

            raise serializers.ValidationError("invalid fee , fee should be greater than 500")

        phone = validated_data.get("phone")

        if len(phone)<9:

            raise serializers.ValidationError("invalid phone number..,phone number has missing digits ... please enter correct phone number ")

        return validated_data


class UserSerializer(serializers.Serializer):

    username = serializers.CharField()

    email = serializers.EmailField()

    password = serializers.CharField()
