from django.urls import path, include
from Student import views
from Student.views import StudentViewApi

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('student', views.StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('apiview/', StudentViewApi.as_view()),
]

#  if generics.api views using the below urls using
# urlpatterns = [
#     path('api/', StudentApi.as_view()),
#     path('api/create/', StudentCreateApi.as_view()),
#     path('api/<int:pk>/', StudentUpdateApi.as_view()),
#     path('api/<int:pk>/delete/', StudentDeleteApi.as_view()),
# ]
