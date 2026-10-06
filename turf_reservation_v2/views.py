from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from django.contrib.auth.models import User

from turf_reservation_v2.serializers import SignupSerilaizer

class SignupView(APIView):

    def post(self,request):

        from_data = request.data

        serializer_instance = SignupSerilaizer(data =from_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            user_object = User.objects.create_user(**cleaned_data)

            serializer_instance = SignupSerilaizer(user_object)

            return Response(data=serializer_instance.data)

        else:

            return Response(data=serializer_instance.errors)


    

        