from django.contrib.auth.models import Group
from rest_framework import viewsets, permissions
from AdminUsers.serializers import UserSerializer, GroupSerializer
from accounts.models import User


"""
Admin must be able to add/list every user in the database. 6. Students must be able to see his information only.
it UserViewSet access only Superuser only
"""
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    """
     API endpoint that allows all admin users to be viewed or edited or deleted.
     """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser, ]
"""
Must define 3 user levels: 1. Super-admin, 2. Teacher, 3. Student (Useinternal Django Groups to achieve the same). 
"""

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited or deleted.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAdminUser, ]
