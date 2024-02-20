#here we will create api endpoint view
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


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

@csrf_exempt
#create function view
def student_create(request):
    if request.method == 'POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer=StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            resp={'msg':'data is created'}
            json_data=JSONRenderer().render(resp)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    
