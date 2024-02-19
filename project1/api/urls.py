from django.urls import path
from . import views
urlpatterns=[
    path("api_home/",views.api_home),
    path("hello/",views.hello),
    path("studinfo/",views.student_list),
    path('studinfo/<int:pk>',views.student_detail)
]