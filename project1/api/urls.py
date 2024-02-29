from django.urls import path
from . import views
urlpatterns=[
    # path("api_home/",views.api_home),
    # path("hello/",views.hello),
    # path("studinfo/",views.student_list),
    # path('studinfo/<int:pk>',views.student_detail),
    # path('student-api/',views.student_api),
    # path('student-api/<int:id>',views.student_api)
    path('student-api/',views.StudentListCreate.as_view()),
    # path('student-create/',views.StudentCreate.as_view()),
    path('student-api/<int:pk>',views.StudentRetrieveUpdateDestroy.as_view())
#     path('student-update/<int:pk>',views.StudentUpdate.as_view()),
#     path('student-delete/<int:pk>',views.StudentDelete.as_view())
 ]