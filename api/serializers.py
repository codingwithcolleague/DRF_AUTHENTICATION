from django.db import models
from django.db.models import fields
from rest_framework import serializers
from api.models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=200)
    
    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name' , instance.name)
        instance.city = validated_data.get('city' , instance.city)
        instance.roll = validated_data.get('roll' , instance.roll)
        instance.save()
        return instance
    
    
    def validate_roll(self,value):
        if value > 200:
            raise serializers.ValidationError("please enter less then your 200")
        return value
    
    def validate_name(self,value):
        if value  == "kiran":
            raise serializers.ValidationError("please enter different name")
        return value
    
    def validate(self, data):
        nm = data.get("name")
        ct = data.get("city")
        if nm.lower() == "rahul" and ct.lower() == "dhanbad":
            raise serializers.ValidationError("City must be different")
        return data 
    
    
class StudentModelSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(read_only=True)
    class Meta:
        model = Student
        fields = ['id' , 'name' , 'roll' , 'city']
        # read_only_fields = [ 'name' , 'roll' ]
        # extra_kwargs = { 'name' :  { 'read_only' : True } }
        
        
    def validate(self, data):
        nm = data.get("name")
        ct = data.get("city")
        print(nm, ct)
        if nm.lower() == "rahul" and ct.lower() == "dhanbad":
            raise serializers.ValidationError("City must be different")
        return data 
    
    def validate_name(self,value):
        if value  == "kiran":
            raise serializers.ValidationError("please enter different name")
        return value