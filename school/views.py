import os
import logging


from pathlib import Path
from django.conf.urls import url

from django.db.models.query import QuerySet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins, generics
from rest_framework import viewsets


from school.models import Student, ClassName
from school.serializers import StudentSerializer, ClassNameSerializer


''' 
BASE_DIR = Path(__file__).resolve().parent.parent

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logging.Formatter(' - %(name)s %(asctime)s - %(levelname)-8s%(reset)s %(blue)s%(message)s')

handler = logging.FileHandler(os.path.join(BASE_DIR,'logs/debug.log'))

logger.addHandler(handler)

logger.error("error message")
logger.info("info message")
logger.warning("warning message") '''
  
"""
class StudentList(APIView):
    def get(self,request, form=None):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self,request, form=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""

"""
#mixins => .list, .create
class StudentList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self,request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

"""

"""
class StudentDetail(APIView):
    def get(self,request, pk, form=None):
        students = Student.objects.get(pk=pk)
        serializer = StudentSerializer(students)
        return Response(serializer.data)

    def put(self,request, pk, form=None):
        students = Student.objects.get(pk=pk)
        serializer = StudentSerializer(students, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        students = Student.objects.get(pk=pk)
        students.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""

"""
#mixins => .retrive, .update, .delete
class StudentDetail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
"""

#Generic class-based views
class StudentList(generics.ListCreateAPIView):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    #print "Merhaba Python!"

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class ClassNameList(generics.ListCreateAPIView):
    
    queryset = ClassName.objects.all()
    serializer_class = ClassNameSerializer
    #logger.info('Sonu??: yeni s??n??f_test eklendi.')

class ClassNameDetail(generics.RetrieveUpdateDestroyAPIView):

    queryset = ClassName.objects.all()
    serializer_class = ClassNameSerializer
