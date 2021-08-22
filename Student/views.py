# Create your views here.
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from Student.models import Students
from Student.serializers import StudentSerializer
from accounts.permissions import Is_Admin, Is_Teacher, Is_student

""" Concrete View Classes
# CreateAPIView
Used for create-only endpoints.
# ListAPIView
Used for read-only endpoints to represent a collection of model instances.
# RetrieveAPIView
Used for read-only endpoints to represent a single model instance.
# DestroyAPIView
Used for delete-only endpoints for a single model instance.
# UpdateAPIView
Used for update-only endpoints for a single model instance.
# ListCreateAPIView
Used for read-write endpoints to represent a collection of model instances.
RetrieveUpdateAPIView
Used for read or update endpoints to represent a single model instance.
# RetrieveDestroyAPIView
Used for read or delete endpoints to represent a single model instance.
# RetrieveUpdateDestroyAPIView
Used for read-write-delete endpoints to represent a single model instance.
"""
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

"""
StudentViewApi readonly is access student if authenticated
"""
class StudentViewApi(generics.ListAPIView, Is_student):
    permission_classes = [IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny, ]
    queryset = Students.objects.all()
    serializer_class = StudentSerializer


"""
After routing has determined which controller to use for a request, your controller is responsible for making sense of the request and producing the appropriate output. Django REST framework allows you to combine the logic 
for a set of related views in a single class, called a ViewSet .
"""
"""
StudentViewset is access only admin,and teacher
"""
class StudentViewSet(ModelViewSet, Is_Admin, Is_Teacher):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser,)

#
# class StudentCreateApi(generics.CreateAPIView, Is_Admin, Is_Teacher):
#     permission_classes = [IsAuthenticated, Is_Admin, Is_Teacher, ]
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializer
#
#
#
#
#
# class StudentUpdateApi(generics.RetrieveUpdateAPIView, Is_Admin, Is_Teacher):
#     permission_classes = [IsAuthenticated, Is_Admin, Is_Teacher, ]
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializer
#
#
# class StudentDeleteApi(generics.DestroyAPIView, Is_Admin, Is_Teacher):
#     permission_classes = [IsAuthenticated, Is_Admin, Is_Teacher, ]
#     queryset = Students.objects.all()
#     serializer_class = StudentSerializer
