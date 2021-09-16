from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from api.models import Student
from api.serializers import StudentModelSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework import status    
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


# Create your views here.

@api_view(['GET','POST','PUT' , 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_api(request,pk=None):
    if request.method == "GET":
        id  = pk
        if id is not None:
            try:
                obj = Student.objects.get(id=id)
                serializers = StudentModelSerializer(obj)
                return Response( serializers.data )
            except Student.DoesNotExist:
                return Response({ "data" : "Object does not exits" })
        obj = Student.objects.all()
        serializers = StudentModelSerializer(obj , many=True)
        return Response(serializers.data)
    
    if request.method == "POST":
        data = request.data
        print("dattaaaaaa" , data)
        serializers = StudentModelSerializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return Response({"msg" : "data created"})
        return Response(serializers.errors)

    if request.method == "PUT":
        id = request.data.get("id")
        obj = Student.objects.get(id=id)
        serializers = StudentModelSerializer(obj , data=request.data, partial = True)
        if serializers.is_valid():
            serializers.save()
            return Response({"msg" : "data updated"})
        return Response(serializers.errors)
    
    if request.method == "DELETE":
        id = request.data.get("id")
        obj = Student.objects.get(id=id)
        obj.delete()
        return Response({ "msg" : "data deleted"  })
    
    
    

class StudentAPI(APIView):
    def get(self,request,pk=None,format=None):
        id  = pk
        if id is not None:
            try:
                obj = Student.objects.get(id=id)
                serializers = StudentModelSerializer(obj)
                return Response( serializers.data )
            except Student.DoesNotExist:
                return Response({ "data" : "Object does not exits" })
        obj = Student.objects.all()
        serializers = StudentModelSerializer(obj , many=True)
        return Response(serializers.data)
    
    def post(self,request,format=None):
        serializers = StudentModelSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            msg = { "msg" : "Data created succesfully" }
            return Response(msg)
        
    def put(self,request,pk=None,format=None):
        id = pk
        try:
            obj = Student.objects.get(id=pk)
            serializers = StudentModelSerializer(obj,data=request.data,partial=True)
            if serializers.is_valid():
                serializers.save()
                msg = { "msg" : "Data  Updated"}
                return Response(msg)
        except Student.DoesNotExist:
            msg = { "msg" : "Data not exits"}
            return Response(msg)
        
    def delete(self,request,pk=None,format=None):
        try:
            obj = Student.objects.get(id=pk)
            obj.delete()
            msg = { "msg" : "Data  Deleted"}
            return Response(msg)
        except Student.DoesNotExist:
            msg = { "msg" : "Data not exits"}
            return Response(msg)
        
    
        
    
    
    
    
    
    