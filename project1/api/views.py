#here we will create api endpoint view
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt


# def api_home(request,*args,**kwargs):
#     return HttpResponse("hello world")
# def hello(request,*args,**kwargs):
#     return JsonResponse({"name":"Samrah"})


# #query set -> all students data
# def student_list(request):
#     stu=Student.objects.all()
#     serializer=StudentSerializer(stu,many=True)
#     json_data=JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data)


# # model instance
# def student_detail(request, pk):
#     stu=Student.objects.get(id= pk)
#     serializer=StudentSerializer(stu)
#     json_data=JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data)

@csrf_exempt
def studentApi(request):
    if request.method=='GET':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return JsonResponse(serializer.data,safe=False) 
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return JsonResponse(serializer.data,safe=False)
    
    if request.method=='POST':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer=StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            resp={'msg':'data created'}
            return JsonResponse(resp,safe=False)
        return JsonResponse(serializer.errors,safe=False)
    
    if request.method=='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            resp={'msg':'data updated'}
            return JsonResponse(resp, safe=False)
        return JsonResponse(serializer.errors,safe=False)
    
    if request.method=='DELETE':
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        resp={'msg':'data deleted'}
        return JsonResponse(resp,safe=False)
        


    
