from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from turf_reservations.models import Bookings
from turf_reservations.serializers import BookingsSerializers
# Create your views here.
class BookingsCreateListView(APIView):

    def get(self,request):

        qs = Bookings.objects.all()

        serializer_instance = BookingsSerializers(qs,many=True)

        return Response(data=serializer_instance.data)
    