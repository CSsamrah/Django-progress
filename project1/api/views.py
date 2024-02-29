#here we will create api endpoint view
from django.http import JsonResponse
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from .models import Student
from .serializers import StudentSerializer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView


#generic concrete api view
# class StudentList(ListAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

class StudentListCreate(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


# class StudentRetrieve(RetrieveAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

# class StudentUpdate(UpdateAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

# class StudentDelete(DestroyAPIView):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer

















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
# @api_view(['GET','POST','PATCH','PUT','DELETE'])
# def student_api(request,id=None):
#     if request.method=='GET':
#         id=id
#         if id is not None:
#             stu=Student.objects.get(id=id)
#             serializer=StudentSerializer(stu)
#             return Response(serializer.data)
#         stu=Student.objects.all()
#         serializer=StudentSerializer(stu,many=True)
#         return Response(serializer.data)
#     if request.method=='POST':
#         serializer=StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
#         return Response(serializer.errors)
#     if request.method=='PUT':
#         id=id
#         stu=Student.objects.get(id=id)
#         serializer=StudentSerializer(stu,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'data updated'})
#         return Response(serializer.errors)
#     if request.method=='PATCH':
#         id=id
#         stu=Student.objects.get(id=id)
#         serializer=StudentSerializer(stu,data=request.data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg':'data partially updated'})
#         return Response(serializer.errors)
#     if request.method=='DELETE':
#         stu=Student.objects.get(id=id)
#         stu.delete()
#         return Response({'msg':'Data deleted'})















# @csrf_exempt
# def studentApi(request):
#     if request.method=='GET':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         python_data=JSONParser().parse(stream)
#         id=python_data.get('id',None)
#         if id is not None:
#             stu=Student.objects.get(id=id)
#             serializer=StudentSerializer(stu)
#             return JsonResponse(serializer.data,safe=False) 
#         stu=Student.objects.all()
#         serializer=StudentSerializer(stu,many=True)
#         return JsonResponse(serializer.data,safe=False)
    
#     if request.method=='POST':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         python_data=JSONParser().parse(stream)
#         serializer=StudentSerializer(data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             resp={'msg':'data is created'}
#             json_data=JSONRenderer().render(resp)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')
    
#     if request.method=='PUT':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         python_data=JSONParser().parse(stream)
#         id=python_data.get('id')
#         stu=Student.objects.get(id=id)
#         serializer=StudentSerializer(stu,data=python_data,partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             resp={'msg':'data updated'}
#             return JsonResponse(resp, safe=False)
#         return JsonResponse(serializer.errors,safe=False)
    
#     if request.method=='DELETE':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         python_data=JSONParser().parse(stream)
#         id=python_data.get('id')
#         stu=Student.objects.get(id=id)
#         stu.delete()
#         resp={'msg':'data deleted'}
#         return JsonResponse(resp,safe=False)
        


    
