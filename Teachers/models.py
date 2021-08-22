from django.db import models

# Create your models here.
from accounts.models import User
from django.db import models

# Create your models here.

class Teacher(models.Model):
    # Role= models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    teacher_name = models.CharField(max_length=100)
    teacher_mobile = models.BigIntegerField()
    teacher_email = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.teacher_name
