from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .serializers import StudentSerializer
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

#class based apiview
class StudentViewSet(viewsets.ViewSet):
    def list(self,request):
            stu=Student.objects.all()
            serializer=StudentSerializer(stu,many=True)
            return Response(serializer.data)
       
    def create(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        
    def update(self,request,pk):
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated'})
        return Response(serializer.errors)
    def partial_update(self,request,pk):
        id=pk
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'partial data updated'})
        return Response(serializer.errors)
    
    def delete(self,request,pk):
        id=pk 
        stu=Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data deleted'})












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








# @api_view(['POST'])
# def hello_world(request):
#     if request.method=='POST':
#         return Response({'msg':'hello  world this is post request'})

# request handler
# Create your views here.
# this request is giving an http response
# def hello(request):
#     return HttpResponse('Hello world') 
#this request will give response as an html template
# def hello(request):
#     return render(request, 'hello.html',{'name':'samrah'})










#class based view using django

# @method_decorator(csrf_exempt,name='dispatch')
# class StudentApi(View):
#     def get(self,request,*args,**kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         python_data=JSONParser().parse(stream)
#         id=python_data.get('id',None)
#         if id is not None:
#             stu=Student.objects.get(id=id)
#             serializer=StudentSerializer(stu)
#             json_data=JSONRenderer().render(serializer.data)
#             return HttpResponse(json_data,content_type='application/json')
#         stu=Student.objects.all()
#         serializer=StudentSerializer(stu, many=True)
#         json_data=JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data,content_type='application/json')
#     def post(self,request,*args,**kwargs):
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
#     def put(self,request,*args,**kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         python_data=JSONParser().parse(stream)
#         id=python_data.get('id')
#         stu=Student.objects.get(id=id)
#         serializer=StudentSerializer(stu,data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             resp={'msg':'data updated!'}
#             json_data=JSONRenderer().render(resp)
#             return HttpResponse(json_data,content_type='application/json')
#         json_data=JSONRenderer().render(serializer.errors)
#         return HttpResponse(json_data,content_type='application/json')

#     def delete(self,request,*args,**kwargs):
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         python_data=JSONParser().parse(stream)
#         id=python_data.get('id')
#         stu=Student.objects.get(id=id)
#         stu.delete()
#         resp={'msg':'data deleted'}
#         json_data=JSONRenderer().render(resp)
#         return HttpResponse(json_data,content_type='application/json')




    


