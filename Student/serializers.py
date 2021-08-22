from rest_framework import serializers

from Student.models import Students

# Serializers define the API representation.
# from accounts.models import User
# from accounts.serializers import RegisterSerializer


class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Students
        # fields = '__all__'
        fields = ('url', 'id', 'stu_name', 'stu_mobile', 'stu_email', 'created_by')
