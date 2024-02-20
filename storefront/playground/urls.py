from django.urls import path
from . import views

urlpatterns=[
    # we use these path functions to create these url pattern object
    path('student-display/',views.student_display),
    path('student-create/',views.student_create)
]