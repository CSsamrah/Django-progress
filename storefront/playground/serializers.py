from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)

    def create(self,validated_data):
        return Student.objects.create(**validated_data)
    def update(self,instance,validated_data):
        print(instance.name)
        instance.name=validated_data.get('name',instance.name)
        print(instance.name)
        instance.roll=validated_data.get('roll',instance.roll)
        instance.city=validated_data.get('city',instance.city)
        instance.save()
        return instance


    
#creating model instance stu

# stu=Student.objects.get(id=1)
# #converting model instance stu to python dict/serializing object
# serializer=StudentSerializer(stu)

# #creating query set
# stu=Student.ojects.all()
# # converting query set stu to list of python dict/serializing query set
# serializer=StudentSerializer(stu,many=True)
# print (serializer.data)