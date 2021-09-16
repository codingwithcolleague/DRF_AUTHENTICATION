from functools import partial
import json
import re
from django.http.response import JsonResponse
from django.shortcuts import render , HttpResponse
from rest_framework.relations import method_overridden
from api.models import Student
from api.serializers import StudentSerializer,StudentModelSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
# Create your views here.
import io
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View



def student_details(request,pk):
    obj = Student.objects.get(id=pk)
    serializer = StudentSerializer(obj)
    # json_data =  JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serializer.data)

def student_list(request):
    obj = Student.objects.all()
    # serializer = StudentSerializer(obj,many=True)
    serializer = StudentModelSerializer(obj,many=True)
    json_data =  JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

@csrf_exempt
def student_create(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = { "msg" : "Data Created" }
            response = JSONRenderer().render(res)
            return HttpResponse(response , content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data , content_type='application/json')
    

@csrf_exempt
def student_update(request):
    if request.method == "PUT":
        body = request.body
        stream = io.BytesIO(body)
        python_data = JSONParser().parse(stream)
        id = python_data.get("id")
        obj = Student.objects.get(id=id)
        serializer = StudentSerializer(obj,data=python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
        res = { "msg" : "data updated" }
        return JsonResponse(res)
        
@csrf_exempt
def studentdelete(request):
    if request.method == "DELETE":
        body = request.body
        stream = io.BytesIO(body)
        python_data = JSONParser().parse(stream)
        id =  python_data.get("id")
        obj = Student.objects.get(id=id)
        obj.delete()
        res = { "msg" : "Data Deleted" }
        data = JSONRenderer().render(res)
        return HttpResponse(data , content_type="application/type")
    
    
@method_decorator(csrf_exempt,name="dispatch")
class StudentAPI(View):
    def get(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get("id",None)
        if id is not None:
            obj = Student.objects.get(id=id)
            serializer = StudentSerializer(obj)
            # json_data =  JSONRenderer().render(serializer.data)
            # return HttpResponse(json_data, content_type='application/json')
            return JsonResponse(serializer.data)
        
        
    def post(self,request,*args,**kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = { "msg" : "Data Created" }
            response = JSONRenderer().render(res)
            return HttpResponse(response , content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data , content_type='application/json')