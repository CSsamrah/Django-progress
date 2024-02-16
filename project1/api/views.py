#here we will create api endpoint view
from django.http import JsonResponse
from django.http import HttpResponse

def api_home(request,*args,**kwargs):
    return HttpResponse("hello world")
def hello(request,*args,**kwargs):
    return JsonResponse({"name":"Samrah"})