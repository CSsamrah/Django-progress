#here we will create api endpoint view
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializer

def api_home(request,*args,**kwargs):
    return HttpResponse("hello world")
def hello(request,*args,**kwargs):
    return JsonResponse({"name":"Samrah"})


#query set -> all students data
def student_list(request):
    stu=Student.objects.all()
    serializer=StudentSerializer(stu,many=True)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data)


# model instance
def student_detail(request, pk):
    stu=Student.objects.get(id= pk)
    serializer=StudentSerializer(stu)
    json_data=JSONRenderer().render(serializer.data)
    return HttpResponse(json_data)
    
