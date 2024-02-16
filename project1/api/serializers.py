from rest_framework import serializers



class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=100)
    roll=serializers.IntegerField()
    city=serializers.CharField(max_length=100)
#creating model instance stu

stu=Student.objects.get(id=1)
#converting model instance stu to python dict/serializing object
serializer=StudentSerializer(stu)

#creating query set
stu=Student.ojects.all()
# converting query set stu to list of python dict/serializing query set
serializer=StudentSerializer(stu,many=True)
print (serializer.data)