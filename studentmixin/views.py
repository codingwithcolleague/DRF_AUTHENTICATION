from django.db.models import query
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import(ListModelMixin,CreateModelMixin,
                                  UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin)
from api.models import Student
from api.serializers import StudentModelSerializer

from rest_framework.generics import (ListAPIView,CreateAPIView,
                                     UpdateAPIView,RetrieveAPIView,DestroyAPIView, 
                                     RetrieveDestroyAPIView, RetrieveUpdateAPIView)

from rest_framework.throttling import ScopedRateThrottle

# Create your views here.
class StudentListMixin(GenericAPIView,ListModelMixin):
    queryset = Student.objects.all()
    # print("yesss")
    # breakpoint()
    serializer_class = StudentModelSerializer
    
    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    
    
class StudentCreateMixin(GenericAPIView,CreateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    

class StudentRetriveMixin(GenericAPIView,RetrieveModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    
    def get(self,request,pk,*args,**kwargs):
        return self.retrieve(request,pk,*args,**kwargs)
    
    

class StudentUpdateMixin(GenericAPIView,UpdateModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    
    def post(self,request,pk,*args,**kwargs):
        return self.update(request,pk,*args,**kwargs)
    

class StudentDestroyMixin(GenericAPIView,DestroyModelMixin):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    
    def delete(self,request,pk,*args,**kwargs):
        return self.destroy(request,pk,*args,**kwargs)
    

class StudentListAPIView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'viewstu'
    

class StudentCreateAPIView(CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    throttle_classes = [ScopedRateThrottle]


class StudentUpdateAPIView(UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope ='modifystu'

    
class StudentRetriveAPIView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    throttle_classes = [ScopedRateThrottle]

    
class StudentDestoryAPIView(DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    
class StudentRetriveDestoryAPIView(RetrieveDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    throttle_classes = [ScopedRateThrottle]

    
class StudentRetriveUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
    throttle_classes = [ScopedRateThrottle]
