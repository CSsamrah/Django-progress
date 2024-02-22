from django.urls import path
from . import views

urlpatterns=[
    # we use these path functions to create these url pattern object
    path('studentapi/',views.StudentApi.as_view())
]