from django.shortcuts import render

# Create your views here.
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from Teachers.models import Teacher
from Teachers.serializers import TeacherSerializer

"""
Teacher must be able to add/list the students. 
"""
class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser,)
