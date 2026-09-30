from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework.response import Response

from turf.models import Turf
from turf.serializers import TurfSerializers,UserSerializer
# Create your views here.


class AdminRegisterView(APIView):

    def post(self,request):

        form_data = request.data

        serializer_instance = UserSerializer(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data = serializer_instance.validated_data

            User.objects.create_superuser(**cleaned_data)

            return Response(data=serializer_instance.validated_data)

        else:

            return Response(data=serializer_instance.errors)

        

class TurfCreateListView(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes=[permissions.IsAdminUser]

    def get(self,request):

        qs = Turf.objects.all()

        serializer_instance = TurfSerializers(qs,many= True)

        return Response(data=serializer_instance.data)

    def post(self,request):

        form_data = request.data

        serialaizer_instance = TurfSerializers(data=form_data)

        if serialaizer_instance.is_valid():

            cleaned_data = serialaizer_instance.validated_data

            Turf.objects.create(**cleaned_data)

            return Response(data=cleaned_data)
        
        else:

            return Response(data=serialaizer_instance.errors)


class TurfRetrieveUpdateDelete(APIView):

    authentication_classes = [authentication.BasicAuthentication]
    permission_classes=[permissions.IsAdminUser]

    def get(self,request,pk=None):

        qs = Turf.objects.get(id=pk)

        serializer_instance = TurfSerializers(qs)

        return Response(data=serializer_instance.data)

    def put(self,request,pk=None):

        form_data = request.data

        serializer_instance = TurfSerializers(data=form_data)

        if serializer_instance.is_valid():

            cleaned_data =serializer_instance.validated_data

            Turf.objects.filter(id=pk).update(**cleaned_data)

            return Response(data=cleaned_data)

        else:

            return Response(data=serializer_instance.errors)

    def delete(self,request,pk = None):

        qs = Turf.objects.get(id=pk).delete()

        return Response(data={"message":"deleted..."})