from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework import authentication,permissions

from django.contrib.auth.models import User

from turf_reservation_v2.serializers import SignupSerilaizer,BookingSerializer
from turf_reservation_v2.models import Booking

from datetime import datetime,time,timedelta

# from turf.models import Turf

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


class BookingCreateListView(APIView):

    authentication_classes =[authentication.BasicAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        qs = Booking.objects.all()

        serializer_instance = BookingSerializer(qs,many=True)

        return Response(data=serializer_instance.data)

    def post(self,request):

        form_data = request.data

        serialzer_instance = BookingSerializer(data=form_data)

        if serialzer_instance.is_valid():

            cleaned_data = serialzer_instance.validated_data

            turf = cleaned_data.get("turf")

            date = cleaned_data.get("date")

            start_time = cleaned_data.get("start_time")

            match_duration = cleaned_data.get("match_duration")

            start_datetime = datetime.combine(date,start_time)

            end_datetime = start_datetime + match_duration

            end_time = end_datetime.time()

            existing_bookings = Booking.objects.filter(turf=turf,date=date,start_time__lt=end_time,end_time__gt=start_time).exists()

            if existing_bookings:

                return Response(data={"error":" Turf is already booked during the selected time "})

            cleaned_data["end_time"] = end_time

            new_booking = Booking.objects.create(**cleaned_data)

            serialzer_instance = BookingSerializer(new_booking)

            return Response(data=serialzer_instance.data)

        else:

            return Response(data=serialzer_instance.errors)

class BookingRetrieveUpdateDeleteView(RetrieveAPIView,UpdateAPIView,DestroyAPIView):

    authentication_classes =[authentication.BasicAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    serializer_class= BookingSerializer

    queryset = Booking.objects.all()



       






    


    

        