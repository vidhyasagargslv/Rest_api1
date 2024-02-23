from django.shortcuts import render
from rest_framework import viewsets
from app_api.models import StudentModel
from app_api.serializers import StudentSerializer


# Create your views here.
#todo we dont use function here , we use rest_frameowrk here for fuctions

class StudentViewSet(viewsets.ModelViewSet):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
