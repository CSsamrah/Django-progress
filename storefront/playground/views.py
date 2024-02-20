from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .serializers import StudentSerializer
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt

# request handler
# Create your views here.
# this request is giving an http response
# def hello(request):
#     return HttpResponse('Hello world') 
#this request will give response as an html template
# def hello(request):
#     return render(request, 'hello.html',{'name':'samrah'})
#serialization
# def student_display(request):
#     data=Student.objects.get(id=1)
#     serializer=StudentSerializer(data)
#     json_data=JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data,content_type='application/json')

#deserialization
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
    


