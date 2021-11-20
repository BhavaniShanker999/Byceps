from re import S
from django.http import request
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from stringapp.models import StringData
from rest_framework import status


# Create your views here.
class AddAndGetStringData(APIView):
    def get(self,request):
        #we can also perform filter operation here
        data = StringData.objects.all().values()
        return Response(data,status.HTTP_200_OK)

    def post(self,request):
        try:
            data =request.data['name']
            if data=="":
                return Response({"message":"string cannot be empty"},status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            pass
        serializer = StringDataSerializer(data=request.data)

        if serializer.is_valid():
            data = serializer.save()
            return Response({"message":"String saved sucessfully","id":data.id},status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status.HTTP_422_UNPROCESSABLE_ENTITY)


class StringOperations(APIView):

    def post(self,request):
        try:
            operation_name = request.data['operation_name'].lower()
            id = request.data['id']
            if operation_name == "":
                return Response({"message":"Operation name cannot be empty"})
            if id == "":
                return Response({"message":"Operation name cannot be empty"})
            data = StringData.objects.get(id =id)
        except:
            return Response({"message":"Invalid operation name or Id"})
       
        def transform_string(string_data):

            mid= len(string_data)//2
            perform_operation={
                                "reverse"      : string_data[-1::-1],

                                "reverse_word" : " ".join( string_data.split(" ")[-1::-1]),

                                "flip"         : string_data[mid::]+string_data[0:mid:],

                                "sort"         : ''.join(sorted(string_data))

                              }

            return (perform_operation[operation_name])

        result = transform_string(data.string_data)
        data.string_data = result
        data.save()

        activity_log = StringDataActivitylog(strind_data_id=data,operation_performed=operation_name,transformed_string_data=result)
        activity_log.save()




        return Response({"data":result},status.HTTP_205_RESET_CONTENT)

class Activitylog(APIView):
    def post(self,request):
        id = request.data['id']
        data = StringDataActivitylog.objects.filter(strind_data_id=id).values()
        if len(data)<1:
            return Response({"message":"No data found."})
        return Response(data)
