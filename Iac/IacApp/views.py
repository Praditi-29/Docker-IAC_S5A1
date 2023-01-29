from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializers
from rest_framework import viewsets
# Create your views here.


class StudentViewSets(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers