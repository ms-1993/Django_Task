"""djangowithjwt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

"""
Task: 
Create REST APIs based on Django with PostgreSQL database. It should contain: 
1. User Sign Up/Forgot Password APIs. 
2. Uses JWT authentication. 
3. Must define 3 user levels: 1. Super-admin, 2. Teacher, 3. Student (Useinternal Django Groups to achieve the same). 
4. Teacher must be able to add/list the students. 
5. Admin must be able to add/list every user in the database. 6. Students must be able to see his information only.

"""
from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    # path('api-auth/', include('rest_framework.urls')),

    # jwt auth
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # jwt urls
    # path('auth/', include('user_registration.urls')),

    # student

    path('Admins/', include('AdminUsers.urls')),
    path('students/', include('Student.urls')),
    path('teachers/', include('Teachers.urls')),


]
