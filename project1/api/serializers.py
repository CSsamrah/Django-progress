from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=['id','name','roll','city']
        def validate_roll(self,value):
            if value>=100:
                raise serializers.ValidationError("no space")
            return value
        def validate_fields(self,data):
            fieldname=data.get('name')
            fieldcity=data.get('city')
            if fieldname.lower()=='samrah' and fieldcity.lower()!='karachi':
                raise serializers.ValidationError('city should be karachi')
            return data



    
    




