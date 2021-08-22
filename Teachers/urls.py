from django.urls import path, include
from Teachers import views
# from Student.views import StudentApi, StudentCreateApi, StudentUpdateApi, StudentDeleteApi

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Teacher', views.TeacherViewSet)

urlpatterns = [
    path('', include(router.urls))
]

#  if generics.api views using the below urls using
# urlpatterns = [
#     path('api/', StudentApi.as_view()),
#     path('api/create/', StudentCreateApi.as_view()),
#     path('api/<int:pk>/', StudentUpdateApi.as_view()),
#     path('api/<int:pk>/delete/', StudentDeleteApi.as_view()),
# ]
