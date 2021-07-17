from school.views import StudentList, StudentDetail, ClassNameList, ClassNameDetail
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('students/', StudentList.as_view()),
    path('students/<int:pk>', StudentDetail.as_view()),
    path('class/', ClassNameList.as_view()),
    path('class/<int:pk>', ClassNameDetail.as_view()),

]
