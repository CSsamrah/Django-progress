from django.shortcuts import render
from django.http import HttpResponse

# request handler
# Create your views here.
# this request is giving an http response
# def hello(request):
#     return HttpResponse('Hello world') 
#this request will give response as an html template
def hello(request):
    return render(request, 'hello.html')