from functools import partial
from django.shortcuts import render
from rest_framework import serializers, viewsets
from api.models import Student
from api.serializers import StudentModelSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication, TokenAuthentication
from rest_framework.permissions import BasePermission, DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, IsAuthenticated,AllowAny,IsAdminUser, IsAuthenticatedOrReadOnly
from api.customepermission import MyPermission
from api.authCust import CustomAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle
from api.throttling import RajRateThrottle

# Create your views here.

class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
        stu = Student.objects.all()
        serializers = StudentModelSerializer(stu , many=True)
        return Response(serializers.data)
        
    def retrieve(self,request,pk=None):
        id = pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializers = StudentModelSerializer(stu)
            return Response(serializers.data)
    
    def create(self,request):
        serializers = StudentModelSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"msg":"Data Created"})
        return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self,request,pk):
        id = pk
        stu = Student.objects.get(id=id)
        serializers = StudentModelSerializer(stu, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response({ serializers.errors })
    
    def destroy(self,request,pk):
        id =pk
        stu = Student.objects.get(id=id)
        stu.delete()
        return Response({ "msg" : "Data Deleted" })
    
    
class StudenModelViewSet1(viewsets.ModelViewSet):
    queryset= Student.objects.all()
    serializer_class = StudentModelSerializer
    # authentication_classes = [BasicAuthentication] #NOt use authentication or non authentocation all are similare
    # permission_classes = [IsAuthenticated]

class StudenModelViewSet2(viewsets.ModelViewSet):
    queryset= Student.objects.all()
    serializer_class = StudentModelSerializer
    # authentication_classes = [BasicAuthentication] #NOt use authentication or non authentocation all are similare
    # authentication_classes = [SessionAuthentication]
    # authentication_classes = [TokenAuthentication]
    # authentication_classes = [CustomAuthentication]
    authentication_classes = [JWTAuthentication]

    # permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    # permission_classes = [MyPermission]
    permission_classes = [IsAuthenticated]

    
class StudenReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset= Student.objects.all()
    serializer_class = StudentModelSerializer
    
    

class StudenModelViewSet(viewsets.ModelViewSet):
    queryset= Student.objects.all()
    serializer_class = StudentModelSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    # throttle_classes = [UserRateThrottle,AnonRateThrottle]
    throttle_classes = [RajRateThrottle,AnonRateThrottle]