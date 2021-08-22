from accounts.models import User
from django.db import models

# Create your models here.

class Students(models.Model):
    # Role = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    stu_name = models.CharField(max_length=100)
    stu_mobile = models.BigIntegerField()
    stu_email = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.stu_name
