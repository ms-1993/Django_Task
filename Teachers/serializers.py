from rest_framework import serializers

from Teachers.models import Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('url', 'id', 'teacher_name', 'teacher_mobile', 'teacher_email', 'created_by')
